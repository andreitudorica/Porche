import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control = 3
GPIO.setup(control,GPIO.OUT)
while(1):
    GPIO.output(control,False)
    time.sleep(2)
    GPIO.output(control,True)
    time.sleep(2)
