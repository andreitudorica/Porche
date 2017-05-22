import math
import RPi.GPIO as GPIO
FrontSensor= [20,21,26,19,13]
LateralSensor= [14,15,18]
EncoderPin=16
ButtonPin=2
GPIO.setup(ButtonPin,GPIO.IN)

for index in xrange(4,-1,-1):
    GPIO.setup(FrontSensor[index], GPIO.IN)
for index in xrange(2,-1,-1):
    GPIO.setup(LateralSensor[index],GPIO.IN)
GPIO.setup(EncoderPin, GPIO.IN)

def getTriggeredSensor():
    TriggeredFrontSensor=0
    for i in xrange(0,4):
	a=GPIO.input(FrontSensor[i])
        TriggeredFrontSensor+=a*pow(2,i)
    return TriggeredFrontSensor

elast = 0
def getLateralSensors():
	sensorLat=0
	for i in xrange(0,3):
		b=GPIO.input(LateralSensor[i])
	sensorLat+=b*pow(2,i)
	return sensorLat

def getButton():
	return GPIO.input(ButtonPin)

def finishDetected():
	return GPIO.input(FrontSensor[4])


def EncoderMPG():
    global elast
    e=GPIO.input(EncoderPin)
    output=0
    if (e==1) & (elast==0):
        output=1
    elast=e
    return output    
