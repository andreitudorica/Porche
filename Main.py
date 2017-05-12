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


import DirectionControl
from DirectionControl import *
from ThrottleControl import *
from UltrasonicSensors import *
from Mapping import *
from PID_follower import correction

time.sleep(2)

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

setTurning(0)
setThrottle(7.9)
to=correction(5)
print to
setTurning(to)
time.sleep(4)
