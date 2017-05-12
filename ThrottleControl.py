import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

ThrottlePin = 26
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PWM(26,50)
ThrottlePin.start(ThrottleAmount)

def setThrottle(ta):
    ThrottleAmount = ta
    ThrottlePin.ChangeDutyCycle(ThrottleAmount) #change Throttle

