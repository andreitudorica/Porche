import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TurningPin = 6
TurningAmount = 7.35
GPIO.setup(TurningPin, GPIO.OUT)
TurningPin = GPIO.PWM(6,50)
TurningPin.start(TurningAmount)


TurningAmount = 7.35
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(1)
TurningAmount = 8.59
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(11)
