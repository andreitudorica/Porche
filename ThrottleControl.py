import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ThrottlePin = 26
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OU)
ThrottlePin = GPIO.PWM(26,50)
ThrottlePin.start(ThrottleAmount)

def setThrottle(ta):
    global ThrottleAmount
    ThrottleAmount = ta
    ThrottlePin.ChangeDutyCycle(ThrottleAmount) #change Throttle

