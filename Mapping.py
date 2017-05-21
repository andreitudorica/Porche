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
    mapping=map(int,f,f.readline().split())
    f.close()

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
