import sys as _sys
import os.path
from DirectionControl import *
from ThrottleControl import *
import RPi.GPIO as GPIO

WheelEncoder = 11
mapping = []
GPIO.setup(WheelEncoder, GPIO.IN)

def readMapping():
    with open('mapping.txt') as f:
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [int(i) for i in line]
                mapping.append(line)

def mappingNeeded():
    return os.path.isfile('mapping.txt')

def mappingDone():
    f=open('mapping.txt','a+')
    for i in xrange(0,mapping.count()):
	print mapping[i]
    	f.write('%d ' %mapping[i])
    f.write('\n')
    f.close()

def mapStep():
    mapping.append(TurningAmount)
