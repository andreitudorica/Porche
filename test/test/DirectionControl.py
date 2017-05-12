import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TurningPin = 6
TurningAmount = 7.35
GPIO.setup(TurningPin, GPIO.OUT)
TurningPin = GPIO.PWM(6,50)
TurningPin.start(TurningAmount)


def setTurning(ta):
    TurningAmount = 7.35 + -1*ta*1.24
    TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
