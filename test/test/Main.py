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

import UltrasonicSensors
import Mapping
import ThrottleControl
import DirectionControl
from DirectionControl import *
from ThrottleControl import *
from UltrasonicSensors import *
from Mapping import *


time.sleep(2)

#RunUltrasonics()
def DummyTest():
	print "throttle 8"
	setThrottle(8)
	print "going straight for 5 seconds"
	setTurning(0)
	time.sleep(5)
	print "turning 1 for 3 seconds"
	setTurning(1)
	time.sleep(3)
	print "turning -1 for 3 seconds"
	setTurning(-1)
	time.sleep(3)
	setThrottle(7.5)

DummyTest()
