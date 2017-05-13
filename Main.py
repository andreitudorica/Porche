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

from DirectionControl import *
from ArduinoInput import *
from ThrottleControl import *
from UltrasonicSensors import *
from Mapping import *
from PID_follower import correction

sensor = 0
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    setTurning(0)

setup()
time.sleep(4)
while 1: 
    sensorBuffer=getTriggeredSensor()
    if sensorBuffer!=0:
        sensor=sensorBuffer
    setTurning(correction(sensor))

GPIO.cleanup()
