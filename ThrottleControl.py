import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


ThrottlePin = 5
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PWM(5,50)
ThrottlePin.start(ThrottleAmount)

def setThrottle(ta):
    global ThrottleAmount
    ThrottleAmount = ta
    ThrottlePin.ChangeDutyCycle(ThrottleAmount) #change Throttle

