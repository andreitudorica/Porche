import sys as _sys
import os.path
from DirectionControl import *
from ThrottleControl import *
import RPi.GPIO as GPIO


WheelEncoder = 11
mapping = []
GPIO.setup(WheelEncoder, GPIO.IN)

def readMapping():
    f=open('mapping.txt','r')
    mapping=map(int,f,readline().split())
    f.close()

def mappingNeeded():
    file=Path('mapping.txt')    
    return file.is_file();

def mappingDone():
    f=open('mapping.txt','w')
    s=str(mapping[0,mapping.count])
    f.write(s)
    f.close()

def mapStep():
    mapping.append(TurningAmount)