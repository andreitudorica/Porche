import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
setup()
import time
GPIO.setmode(GPIO.BCM)
import sys as _sys
try:
    import threading as _threading
    from threading import Thread
except ImportError:
    del _sys.modules[__name__]
    raise

from DirectionControl import *
from ArduinoInput import *
from ThrottleControl import *
from UltrasonicSensors import *
from Mapping import *
from PID_follower import correction

time.sleep(2)
# 13,19,26,21,20 front sensors
#16 wheel spin
# echo = [17,22,9]
# trig = [4,27,10]
#14,15,18 sensori laterali
#RunUltrasonics()
def DummyTest():
	print "throttle 7.9"
	setThrottle(7.9)
	print "going straight for 3 seconds"
	setTurning(-1)
	time.sleep(5)
#	print "turning 1 for 3 seconds"
#	setTurning(1)
#	time.sleep(1)
#	print "turning -1 for 3 seconds"
#	setTurning(-1)
#	time.sleep(1)
	setThrottle(7.5)

time.sleep(2);
#setTurning(0)
#setThrottle(7.9)
#setTurning(1)
getTriggeredSensor()
#to=correction(5)
#print to
#setTurning(to)
#time.sleep(4)
GPIO.cleanup()
