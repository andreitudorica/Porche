import RPi.GPIO as GPIO
FrontSensor= [13,19,26,21,20]
for index in xrange(0,4):
    GPIO.setup(FrontSensor[index], GPIO.IN)
def getTriggeredSensor():
    TriggeredFrontSensor=FrontSensor[0]+2*FrontSensor[1]+4*FrontSensor[2]+8*FrontSensor[3]+16*FrontSensor[4];
    print TriggeredFrontSensor
    return TriggeredFrontSensor