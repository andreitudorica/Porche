import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

ThrottlePin = 5
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PwM(5,50)
ThrottlePin.start(ThrottleAmount)


ThrottleAmount = 7.8
ThrottlePin.ChangeDutyCycle(ThrottleAmmount) #change Throttle
time.sleep(1.5)
ThrottleAmount = 7.5
