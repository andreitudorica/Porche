import math
import RPi.GPIO as GPIO
FrontSensor= [20,21,26,19,13]
for index in xrange(4,-1,-1):
    GPIO.setup(FrontSensor[index], GPIO.IN)
def getTriggeredSensor():
    TriggeredFrontSensor=0
    for i in xrange(0,5):
	a=GPIO.input(FrontSensor[i])
        TriggeredFrontSensor+=a*pow(2,i)
    return TriggeredFrontSensor
