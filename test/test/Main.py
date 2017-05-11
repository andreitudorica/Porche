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

from UltrasonicSensors import *
from Mapping import *




refresh_thread = Thread(target=refresh_sensors)#define separate thread for ultrasonic sensors read
refresh_thread.start()
while 1:
    event.clear()
    for index in xrange(0, nr_ultrasonic_sensors):
        print sensor_readings[index]
    #if mappingDone()==False & WheelEncoder==1:
    #    mapStep()
    time.sleep(0.5)
    event.set()

    print"\n"

GPIO.cleanup()