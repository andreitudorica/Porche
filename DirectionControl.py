
import RPi.GPIO as GPIO

TurningPin = 6
NullTurning = 7.12
TurningDelta = 1.5
TurningAmount = NullTurning
GPIO.setup(TurningPin, GPIO.OUT)
TurningPin = GPIO.PWM(6,50)
TurningPin.start(TurningAmount)



def setTurning(ta):
    global TurningAmount
    if (ta > 0.3) | (ta < -0.3):
	    delta = -0.5
    else:
	    delta = 0
    TurningAmount = NullTurning - ta*TurningDelta
    TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
