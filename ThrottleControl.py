import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


ThrottlePin = 5
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PWM(5,1000)
ThrottlePin.start(ThrottleAmount)

def setThrottle(ta):
    global ThrottleAmount
    ThrottleAmount = ta
    ThrottlePin.ChangeDutyCycle(ta) #change Throttle

