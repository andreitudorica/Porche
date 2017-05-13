from __future__ import division
last_position = 0
center_sensor=5
nr_sensors=9
Kp=10
Ki=5
Kd=1.2
lerror = 0 #last error
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
    global lerror
    lerror = error

def correction(raw_position):
    print lerror
    position=current_position(raw_position)
    error=calculate_error(position)
    motor_direction=Kp*error+Kd*(error-lerror)
    max_direction=Kp*4+4*Kd #compute the max rotation to normalize
    print motor_direction
    print max_direction
    direction = motor_direction / max_direction
    set_last_error(error)



    return direction



print correction(2)



