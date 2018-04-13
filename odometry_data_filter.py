#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

def odometry_data_filter(n_l, n_r):

    motor_l = ev3.LargeMotor('outB')
    motor_r = ev3.LargeMotor('outC')
    if (n_l*n_r)>0 :
        n=(n_l+n_r)/2
        trans= 0.048*n
        rot=0
    else:
        n = (abs(n_l) + abs(n_r)) / 2
        if n_r == 0:
            rot = 0
            trans = 0
        else:
            rot = (n_r/abs(n_r))*0.5385*n
            trans=0

    motor_l.reset()
    motor_r.reset()
        
    return trans, rot


