#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

def rotate_sensor():
    us = ev3.UltrasonicSensor()
    us.mode='US-DIST-CM'
    units = us.units
    distance = us.value()/10
    X = []
    
    motor_sensor = ev3.MediumMotor('outD')
    motor_sensor.reset()
    
    motor_sensor.run_to_rel_pos(position_sp=-180, speed_sp=60, stop_action="brake")
    tick = motor_sensor.position
    count = 0
    tick_last = 0
    while count < 90:
        tick = motor_sensor.position
        if tick % 2 == 0 and tick != tick_last:
            distance = us.value()/10
            X.append(distance)
            print(str(distance))
            tick_last = tick
    
            count = len(X)

    sleep(4)
    motor_sensor.run_to_rel_pos(position_sp=180, speed_sp=200, stop_action="brake")
