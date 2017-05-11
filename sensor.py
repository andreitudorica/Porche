import RPi.GPIO as GPIO
from threading import Thread
import time
GPIO.setmode(GPIO.BCM)
import sys as _sys
try:
    import threading as _threading
except ImportError:
    import dummy_threading as _threading

except ImportError:
    del _sys.modules[__name__]
    raise



nr_ultrasonic_sensors=3
echo=[17,22,9]
trig=[4,27,10]


sensor_readings=[]
print "Waiting For Sensors To Settle"
time.sleep(2)
def setup_ultrasonics():
    for index in xrange(0, nr_ultrasonic_sensors):
        sensor_readings.append(0)
        GPIO.setup(echo[index], GPIO.IN)
        GPIO.setup(trig[index], GPIO.OUT)
        GPIO.output(trig[index], False)

def read_ultrasonics():
    for index in xrange(0, nr_ultrasonic_sensors):

        GPIO.output(trig[index], True)
        time.sleep(0.00001)
        GPIO.output(trig[index], False)

        while GPIO.input(echo[index]) == 0:
            pulse_start = time.time()
        while GPIO.input(echo[index]) == 1:
            pass

        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance=round(pulse_duration * 17150, 2)
        if(distance<300):
            sensor_readings[index]=distance
        time.sleep(0.00001)
semaphore = _threading.BoundedSemaphore()

def refresh_sensors():

    while 1:
        event.wait()
        read_ultrasonics()

    print"Ready reading"
    return 0.2
GPIO.setwarnings(False)
setup_ultrasonics()
print "ready setup"
event = _threading.Event()
refresh_thread=Thread(target=refresh_sensors)
refresh_thread.start()
while 1:
    event.clear()
    for index in xrange(0, nr_ultrasonic_sensors):
        print sensor_readings[index]
    time.sleep(0.5)
    event.set()

    print"\n"

GPIO.cleanup()

print "Ready"