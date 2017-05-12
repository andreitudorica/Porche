import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

ThrottlePin = 26
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PWM(26,50)
ThrottlePin.start(ThrottleAmount)

time.sleep(2)
ThrottleAmount = 8
ThrottlePin.ChangeDutyCycle(ThrottleAmount) #change Throttle
time.sleep(10)
ThrottleAmount = 7.5
ThrottlePin.ChangeDutyCycle(ThrottleAmount) #change Throttle

