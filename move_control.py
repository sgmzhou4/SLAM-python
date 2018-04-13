#!/usr/bin/env python3


import ev3dev.ev3 as ev3
from time import sleep

def go_line(position, speed):
    motor_l = ev3.LargeMotor('outB')
    motor_r = ev3.LargeMotor('outC')
    motor_l.reset()
    motor_r.reset()
    motor_l.run_to_rel_pos(position_sp=position, speed_sp=speed, stop_action="brake")
    motor_r.run_to_rel_pos(position_sp=position, speed_sp=speed, stop_action="brake")
    time = position/speed + 1
    sleep(int(time))

    return motor_l.position, motor_r.position

def rotate(position, speed):
    motor_l = ev3.LargeMotor('outB')
    motor_r = ev3.LargeMotor('outC')
    motor_l.reset()
    motor_r.reset()
    motor_l.run_to_rel_pos(position_sp=position, speed_sp=speed, stop_action="hold")
    motor_r.run_to_rel_pos(position_sp=-position, speed_sp=speed, stop_action="hold")
    time = position/speed + 1
    sleep(int(time))

    return motor_l.position, motor_r.position
