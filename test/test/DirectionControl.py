TurningPin = 6
TurningAmount = 7.5
GPIO.setup(TurningPin, GPIO.OUT)
TurningPin = GPIO.PVM(5,50)
TurningPin.start(TurningAmount)


TurningAmount = 6.11
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(1)
TurningAmount = 8.89
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(1)
TurningAmount = 6.11
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(1)
TurningAmount = 8.89
TurningPin.ChangeDutyCycle(TurningAmount) #change Throttle
time.sleep(1)
