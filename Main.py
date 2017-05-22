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

#start=1
#while start!=0:
#	start=getButton()	

sensor = 5
delta = 0
speedSet = 0
stepCounter = 0
Sum = 0
global mappingOn
mappingOn=False

setThrottle(0)

def setup():
	global mappingOn
    	GPIO.setmode(GPIO.BCM)
    	GPIO.setwarnings(False)
    	setTurning(0)
#    	print "mapping needed", mappingNeeded()
#    	if mappingNeeded()==False:
#		mappingOn=True
#    	else:
#		mappingOn=False
#		readMapping()
setup()
time.sleep(4)
t=time.time()
LastMPG=time.time()
lp=0
lthrot=0
basicThrottle = 40          #the basic level of throttle
simulationLength = 420      #number of seconds the code runs
numberOfStepsToAverage = 1 #the number of steps that are recorded to compute the change in throttle
minimalDiff = 0.005        #the minimal trusted difference between 2 encoder steps 
DesiredGap = 0.06          #the desired gap between 2 steps



currentIndex=0

global engage
engage=False

engagingTime= 0.65
engageLeft=-1
engageRight=1
dischargeLeft=2
dischargeRight=8

SpeedSetIncrease = 0.4 
SpeedSetDecrease = 0.3
SpeedSetMin=-20
SpeedSetMax=20
setCenterSensor(5)
RunUltrasonics()
#while 1==1:
#	time.sleep(0.3)
#	ultrasonics=[0,0,0]
#	ultrasonics=getUltrasonics()
#	if ultrasonics[0]!=0 and ultrasonics[1]!=0 and ultrasonics[2]!=0:
#		print ultrasonics[0],' ',ultrasonics[1],' ',ultrasonics[2]
global obstacleDetected
global demoDone
global lastTurningAmount
engageTurns=0
setEngageTimer=False
global lastUltrasonicRead
lastUltrasonicRead=time.time()

obstacleDetected=False
demoDone=False
lastTurningAmount=0
ultrasonics=[0,0,0]
step=0
while time.time()<t+simulationLength:
#	if getButton()==0:
#		break
#	print "Steeeeep ",step
#	print "Time interval for sensors ",time.time()-lastUltrasonicRead
#	if time.time()-lastUltrasonicRead>0.03:
##		ultrasonics[step]=read_ultrasonics(step)
#		step=step+1
#		print "Steeeeep ",step
		#0-right 1-middle 2-left
#		if step==3:
#			step=0
#			if ultrasonics[0]!=None and ultrasonics[1]!=None and ultrasonics[2]!=None:
#				print ultrasonics
#				if ultrasonics[0] < 30 and ultrasonics[1] < 30 and engage == False: #object in middle-right side
#					print 'ENGAGE'
#					engage=True
#					engageTurns=8
#					sensor=dischargeRight
#					decidedEngage=engageLeft
#		lastUltrasonicRead=time.time()
#	if finishDetected()==1 and mappingOn==True:
#		mappingOn=False
#		mappingDone()
#		currentIndex=0
#		setThrottle(0)
#		print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
	#print EncoderMPG()
	if (EncoderMPG() == 1) & (time.time() - LastMPG>minimalDiff):
		CurrMPG = time.time()
		if engage==True:
			engageTurns -= 1
			print engageTurns
		Sum = CurrMPG - LastMPG
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
		LastMPG=CurrMPG
#		if mappingOn==True:
                        #print 'maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaap'
 #                       mapStep(lastTurningAmount)
#		else:
#			currentIndex=currentIndex+1
	#lateralSensor=getLateralSensors()
	lateralSensor=0
	if engage==False and lateralSensor==0:#normal case
		#print "NORMAL CASE"
		sensorBuffer=getTriggeredSensor() # get the triggered front sensor in a buffer
 		#print "Position of last sensorBuffer---------",sensorBuffer,time.time()
	    	if (sensorBuffer!=0) & (abs(sensor-sensorBuffer)<3): #if it is not 0
        	    	if sensor!=sensorBuffer:#we set the change the sensor we decide the turning on
	    			print "Position of last sensor---------",sensor
				sensor=sensorBuffer
	    	ComputedCorrection=correction(sensor) # compute the correction 
	    	setTurning(ComputedCorrection) # set turning acording to the front sensors
		lastTurningAmount=ComputedCorrection
	else:
		#if lateralSensor==0:#in collision avoidance state
			if(engageTurns>0):#if in engage state
#				print engageTurns
				setTurning(decidedEngage)# engage
				lastTurningAmount=decidedEngage
			else:
				engage=False
				setEngageTimer=False	
				print "Finalizare depasire, hihi finalizare :>"
		#else:
			#if lateralSensor==2 or lateralSensor==1:
			#	setTurning(1)
			#	print "LEEEEEEEEEEEFT"
			#if lateralSensor==3 or lateralSensor==4:
			#	setTurning(-1)
			#	print "RIGHTTTTTTTTTT"

    	if engage==True:
        	speedSet=-4
	throt= basicThrottle + speedSet #compute the new throttle
	if throt != lthrot:
		setThrottle(throt)
		print "Throtle ",throt
		lthrot=throt
print "Stop"

GPIO.cleanup()
