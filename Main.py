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
engage=False
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    setTurning(0)

setup()
time.sleep(4)
time.sleep(0.1)
t=time.time()
LastMPG=time.time()
lp=0
lthrot=0
basicThrottle = 20       #the basic level of throttle
simulationLength = 100     #number of seconds the code runs
numberOfStepsToAverage = 1 #the number of steps that are recorded to compute the change in throttle
minimalDiff = 0.005        #the minimal trusted difference between 2 encoder steps 
DesiredGap = 0.05          #the desired gap between 2 steps
SpeedSetIncrease = 1 
SpeedSetDecrease = 1
SpeedSetMin=-20
SpeedSetMax=20
setCenterSensor(5)
while time.time()<t+100:
    if time.time()>5 & engage==False:
        secondTimer=time.time()
        while time.time()<secondTimer+2
            setTurning(-1)
            setThrottle(basicThrottle)
        secondTimer=time.time()
        while time.time()<secondTimer+2
            setTurning(1)
            setThrottle(basicThrottle)
        engage=True
	if (EncoderMPG() == 1) & (time.time() - LastMPG>minimalDiff):
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
        sensorBuffer=getTriggeredSensor() # get the triggered front sensor in a buffer
	if (sensorBuffer!=0) & (abs(sensor-sensorBuffer)<3): #if it is not 0
        	sensor=sensorBuffer#we set the change the sensor we decide the turning on
	ComputedCorrection=correction(sensor) # compute the correction 
	setTurning(ComputedCorrection) # set turning acording to the front sensors
	throt= basicThrottle + speedSet #compute the new throttle
	if throt != lthrot:
		setThrottle(throt)
		print "Throtle ",throt
		lthrot=throt
print "Stop"

GPIO.cleanup()
