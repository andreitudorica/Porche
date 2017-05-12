import sys as _sys
import Main
from Main import *


WheelEncoder = 11
GPIO.setup(WheelEncoder, GPIO.IN)

def mappingDone():
    return False;

def mapStep():
    print TurningAmount