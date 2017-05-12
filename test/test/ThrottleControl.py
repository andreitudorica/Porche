import time
ThrottlePin = 5
ThrottleAmount = 7.5
GPIO.setup(ThrottlePin, GPIO.OUT)
ThrottlePin = GPIO.PVM(5,50)
ThrottlePin.start(ThrottleAmount)


ThrottleAmount = 7.5
ThrottlePin.ChangeDutyCycle(ThrottleAmmount) #change Throttle
time.sleep(1)
ThrottleAmount = 9
ThrottlePin.ChangeDutyCycle(ThrottleAmmount) #change Throttle
time.sleep(1)
ThrottleAmount = 7.5
ThrottlePin.ChangeDutyCycle(ThrottleAmmount) #change Throttle
time.sleep(1)
ThrottleAmount = 9
ThrottlePin.ChangeDutyCycle(ThrottleAmmount) #change Throttle
time.sleep(1)
