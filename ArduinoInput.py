import math
import RPi.GPIO as GPIO
FrontSensor= [20,21,26,19,13]
EncoderPin=16
for index in xrange(4,-1,-1):
    GPIO.setup(FrontSensor[index], GPIO.IN)
GPIO.setup(EncoderPin, GPIO.IN)
def getTriggeredSensor():
    TriggeredFrontSensor=0
    for i in xrange(0,5):
	a=GPIO.input(FrontSensor[i])
        TriggeredFrontSensor+=a*pow(2,i)
    return TriggeredFrontSensor

elast = 0
def EncoderMPG():
    global elast
    e=GPIO.input(EncoderPin)
    output=0
    if (e==1) & (elast==0):
        output=1
    elast=e
    return output    
