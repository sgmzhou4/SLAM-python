#!/usr/bin/env python3

#import ev3dev.ev3 as ev3
from time import sleep
import numpy as np

def centre_line_finder(_angle2):

    angle_0 = (_angle2 - 0)
    angle_90 = (_angle2 - 90)
    angle_180 = (_angle2 - 180)
    angle_270 = (_angle2 - 270)

    angle = np.array([abs(angle_0), abs(angle_90), abs(angle_180), abs(angle_270)])
    
    x = angle.argmin()
    e_angle = angle[x]
    c_angle = 0

    if x == 0:
        e_angle = angle_0
        c_angle = 0
    elif x == 1:
        e_angle = angle_90
        c_angle = 90
    elif x == 2:
        e_angle = angle_180
        c_angle = 180
    elif x == 3:
        e_angle = angle_270
        c_angle = 270
        
    return e_angle, c_angle

