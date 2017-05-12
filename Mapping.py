import sys as _sys
from DirectionControl import *
from ThrottleControl import *
import RPi.GPIO as GPIO

# import Main
# from Main import *


WheelEncoder = 11
GPIO.setup(WheelEncoder, GPIO.IN)

def mappingDone():
    return False;

def mapStep():
    print TurningAmount
