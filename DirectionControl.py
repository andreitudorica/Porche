
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TurningPin = 6
NullTurning = 7.12
TurningDelta = 1.5
TurningAmount = NullTurning
GPIO.setup(TurningPin, GPIO.OUT)
TurningPin = GPIO.PWM(6,50)
TurningPin.start(TurningAmount)


def setTurning(ta):
    global TurningAmount
    TurningAmount = NullTurning - ta*TurningDelta
    TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
