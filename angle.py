#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

m = ev3.LargeMotor('outB')
n = ev3.LargeMotor('outC')



gy = ev3.GyroSensor() 
gy.mode='GYRO-ANG'
units = gy.units


angle_1 = gy.value()

sleep(2)

m.run_to_rel_pos(position_sp=4500, speed_sp=300, stop_action="hold")

sleep(18)

angle_2 = gy.value()

angle = angle_2 - angle_1
sleep(2)

print(str(angle) + " " + units)
    
sleep(2)
