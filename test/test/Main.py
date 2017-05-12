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

RunUltrasonics()
setThrottle(8)
setTurning(0)
time.sleep(1)
setTurning(-1)
time.sleep(3)
setThrottle(7.5)