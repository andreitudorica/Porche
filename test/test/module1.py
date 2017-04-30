import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG1 = 4
ECHO1 = 17

TRIG2 = 27
ECHO2 = 22

TRIG3 = 10
ECHO3 = 9

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)

GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
GPIO.output(TRIG3, False)

print "Waiting For Sensors To Settle"
time.sleep(2)

for index in (0, 10):
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)

    while GPIO.input(ECHO1)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO1)==1:
        pulse_end = time.time()  
    pulse_duration = pulse_end - pulse_start

    distance = round(pulse_duration * 17150, 2)
    print "Distance1:",distance,"cm"

    time.sleep(0.3);

    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)

    while GPIO.input(ECHO2)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO2)==1:
        pulse_end = time.time()  
    pulse_duration = pulse_end - pulse_start

    distance = round(pulse_duration * 17150, 2)
    print "Distance2:",distance,"cm"

    time.sleep(0.3);

    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)

    while GPIO.input(ECHO3)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO3)==1:
        pulse_end = time.time()  
    pulse_duration = pulse_end - pulse_start

    distance = round(pulse_duration * 17150, 2)
    print "Distance3:",distance,"cm"

    time.sleep(0.3)

GPIO.cleanup()