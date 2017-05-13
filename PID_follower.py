from __future__ import division
last_position = 0
center_sensor=5
nr_sensors=9
Kp=3
Ki=1
Kd=0#changed from 2
lerror = 0 #last error
prevtime = 0 
def calculate_error(position):

    return position -center_sensor
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

    currtime = time.time()
    dt = currtime - prevtime
    position=current_position(raw_position)
    error=calculate_error(position)
    if dt > 0:
        motor_direction=Kp*error+Kd*(error-lerror) / dt
    else:
        motor_direction=Kp*error+Kd*(error-lerror)
    max_direction=Kp*4+4*Kd #compute the max rotation to normalize
    direction = motor_direction / max_direction
    set_last_error(error)
    prevtime = currtime

    return direction







