import time
import sys as _sys
try:
    import threading as _threading
    from threading import Thread
except ImportError:
    del _sys.modules[__name__]
    raise

def fcnObstacleAvoidance():
        from Main import engage,sensor
      	while time.time()<secondTimer+0.65:
            	setTurning(1)
            	#setThrottle(basicThrottle+5)
		print "Back on track////////////"
		
		setThrottle(basicThrottle)
		print "last sensor///////// ",sensor
		print "Finished depasire//////////"
        global obstacleDetected
        obstacleDetected=False

def runObstacleAvoidance():
    	startObstacle = Thread(target=fcnObstacleAvoidance)#define separate thread for ObstacleAvoidance
    	startObstacle.start()
