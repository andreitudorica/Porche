import time
from Main import *
import sys as _sys
try:
    import threading as _threading
    from threading import Thread
except ImportError:
    del _sys.modules[__name__]
    raise

def  ObstacleAvoidance():
        
		print "Started depasire///////////////// "
      	secondTimer=time.time()
      	while time.time()<secondTimer+0.65:
            setTurning(1)
            #setThrottle(basicThrottle+5)
		print "Back on track////////////"
		engage=True
		sensor=2
		setThrottle(basicThrottle)
		print "last sensor///////// ",sensor
		print "Finished depasire//////////"
        global obstacleDetected
        obstacleDetected=False

def runObstacleAvoidance():
    startObstacle = Thread(target=ObstacleAvoidance)#define separate thread for ultrasonic sensors read
    startObstacle.start()