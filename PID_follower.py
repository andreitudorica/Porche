last_position = 0
center_sensor=5
nr_sensors=9
Kp=10
Ki=5
Kd=5
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
         1.5:10,
         2.5:11,
         3.5:12,
         4.5:13,
         5.5:14,
         6.5:15,
         7.5:16,
         8.5:17,
        }
    return pos[coded_position]
def set_last_error(error):
    global lerror
    lerror = error
    print Kp
def correction(raw_position):
    position=current_position(raw_position)
    error=calculate_error(position)
    motor_direction=Kp*calculate_error(position)+Kd*(error-lerror)
    max_direction=Kp*4+4*Kd
    set_last_error(error)
    return motor_direction/max_direction







