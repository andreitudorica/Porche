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



RunUltrasonics()

while 1:
    printUltrasonics()
    if mappingDone()==False:
        mapStep()