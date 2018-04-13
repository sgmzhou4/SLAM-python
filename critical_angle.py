#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep


def critical_angle(position,speed):
    motor_sensor = ev3.MediumMotor('outD')
    motor_sensor.run_to_rel_pos(position_sp=position, speed_sp=speed, stop_action="hold")
    time = position/speed + 1
    sleep(int(time))
    
