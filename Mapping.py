import sys as _sys
import os.path
from DirectionControl import *
from ThrottleControl import *
import RPi.GPIO as GPIO
import array as array
WheelEncoder = 11
mapping = array.array('f')
GPIO.setup(WheelEncoder, GPIO.IN)

def readMapping():
    	with open('mapping.txt') as f:
        	for line in f:
            		line = line.split() # to deal with blank 
            		if line:            # lines (ie skip them)
				for i in line:
                			mapping.append(float(i))
    	print 'mapping:'
    	for i in xrange(0,mapping.buffer_info()[1]):
		print mapping[i]

def mappingNeeded():
	return os.path.isfile('mapping.txt')

def mappingDone():
	f=open('mapping.txt','a+')
        for i in xrange(0,mapping.buffer_info()[1]):
                print mapping[i]
		f.write('%f ' %mapping[i])
   	f.write('\n')
   	f.close()

def mapStep(ta):
   	print 'map step :::::::::::::::::::',ta
   	mapping.append(float(ta))
