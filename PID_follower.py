from __future__ import division
import time as time
last_position = 0
center_sensor=5
nr_sensors=9
Kp=300
Ki=1
Kd=100#changed from 2
lerror=0 #last error
prevtime=time.time() 
def calculate_error(position):
    return position -center_sensor
def setCenterSensor(sensor):
	global center_sensor
	if sensor==5:
		Kp=5
		Ki=1
		Kd=50
	else:
		Kp=7
		Ki=1
		Kd=25	
	center_sensor=sensor
def  current_position(coded_position): #get the current position
    pos={0:center_sensor,
         1:1,
         2:2,
         3:3,
         4:4,
         5:5,
         6:6,
         7:7,
         8:8,
         9:9,
         10:1.5,
         11:2.5,
         12:3.5,
         13:4.5,
         14:5.5,
         15:6.5,
         16:7.5,
         17:8.5,
        }
    return pos[coded_position]
def set_last_error(error):
    lerror = error

def correction(raw_position):

    currtime=time.time()
    global prevtime
    global last_position
    dt=currtime-prevtime
    position=current_position(raw_position)
    if position != last_position:
        print "position: ", position
    error=calculate_error(position)
    if dt > 0:
        motor_direction=Kp*error+Kd*(error-lerror) / dt 
    	#print "Motor Direction: ", dt
    else:
    	motor_direction=Kp*error+Kd*(error-lerror)
    delta=5-abs(5-center_sensor)-1;
    max_direction=Kp*delta+delta*Kd/dt #compute the max rotation to normalize
    direction = motor_direction / max_direction
    set_last_error(error)
    prevtime = currtime
    last_position=position
    return direction







