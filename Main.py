import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import sys as _sys
try:
    import threading as _threading
    from threading import Thread
except ImportError:
    del _sys.modules[__name__]
    raise
import PID_follower 
from DirectionControl import *
from ArduinoInput import *
from ThrottleControl import *
from UltrasonicSensors import *
from Mapping import *
from PID_follower import *

sensor = 5
delta = 0
speedSet = 0
stepCounter = 0
Sum = 0
global mappingOn
mappingOn=False
engage=False

setThrottle(0)
def finishDetected():
	global fd
	if fd==1:	
		fd=0
		return True
	return False

def setup():
	global mappingOn
    	GPIO.setmode(GPIO.BCM)
    	GPIO.setwarnings(False)
    	setTurning(0)
    	print "mapping needed", mappingNeeded()
    	if mappingNeeded()==False:
		mappingOn=True
    	else:
		mappingOn=False
		readMapping()
setup()
time.sleep(4)
t=time.time()
LastMPG=time.time()
lp=0
lthrot=0
basicThrottle = 22          #the basic level of throttle
simulationLength = 100      #number of seconds the code runs
numberOfStepsToAverage = 1 #the number of steps that are recorded to compute the change in throttle
minimalDiff = 0.005        #the minimal trusted difference between 2 encoder steps 
DesiredGap = 0.05          #the desired gap between 2 steps

engagingTime=0.65
engageLeft=-1
engageRight=1
dischargeLeft=2
dischargeRight=8

SpeedSetIncrease = 0.3 
SpeedSetDecrease = 0.3
SpeedSetMin=-20
SpeedSetMax=20
setCenterSensor(5)
RunUltrasonics()
global fd
global obstacleDetected
global demoDone
global lastTurningAmount
fd=0
obstacleDetected=False
demoDone=False
lastTurningAmount=0
while time.time()<t+simulationLength:
	if time.time()>t+4 and demoDone==False:       #demo collision avoidance     
	        print "Started depasire///////////////// "
        	engageStart=time.time()
		obstacleDetected=True
            	engage=True
		sensor=dischargeLeft
		decidedEngage=engageRight

		demoDone=True

	if finishDetected()==True and mappingOn==True:
		mappingOn=False
		mappingDone()
	#print EncoderMPG()
	if (EncoderMPG() == 1) & (time.time() - LastMPG>minimalDiff):
#		print 11111111
		CurrMPG = time.time()
		stepCounter += 1
		Sum = Sum + CurrMPG - LastMPG
		if (stepCounter == numberOfStepsToAverage):
			Gap = Sum / numberOfStepsToAverage #compute average gap
      			if Gap < DesiredGap: #if the gap is too small
           			speedSet -= SpeedSetDecrease # slow down
				if speedSet < SpeedSetMin:
					speedSet = SpeedSetMin
        		else: #if the gap is too big
				speedSet += SpeedSetIncrease #speed up
				if speedSet > SpeedSetMax:						
					speedSet = SpeedSetMax
			print "MPG: " , Gap , "SpeedSet: " , speedSet
			stepCounter = 0 #reset counter
			Sum = 0 #reset sum
		LastMPG=CurrMPG
		if mappingOn==True:
                        print 'maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaap'
                        mapStep(lastTurningAmount)

	if engage==False:#normal case
		sensorBuffer=getTriggeredSensor() # get the triggered front sensor in a buffer
	    	if (sensorBuffer!=0) & (abs(sensor-sensorBuffer)<3): #if it is not 0
        	    	sensor=sensorBuffer#we set the change the sensor we decide the turning on
	    		#print "Position of last sensor",sensor
	    	ComputedCorrection=correction(sensor) # compute the correction 
	    	setTurning(ComputedCorrection) # set turning acording to the front sensors
		lastTurningAmount=ComputedCorrection
	else :#in collision avoidance state
		if(time.time()<engageStart+engagingTime):#if in engage state
			setTurning(decidedEngage)# engage
			lastTurningAmount=decidedEngage
		else:
			engage=False
			fd=1	
    	if engage==True:
        	speedSet=-4
	throt= basicThrottle + speedSet #compute the new throttle
	if throt != lthrot:
		setThrottle(throt)
		print "Throtle ",throt
		lthrot=throt
print "Stop"

GPIO.cleanup()
