#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep
import numpy as np

def perception_data_filter(distance, distance_angle, e_angle):
    if e_angle > 0:
        left_line = 180 - e_angle
        right_line = 0
    else:
        left_line = 180
        right_line = - e_angle

    mean_left = distance[(left_line/2) : (left_line/2 - 5)].mean()
    var_left = distance[(left_line/2) : (left_line/2 - 5)].var()
    mean_right = distance[(right_line/2) : (right_line/2 + 5)].mean()
    var_right = distance[(right_line/2) : (right_line/2 + 5)].var()

    L = distance._len_()

    left_critical = 0
    right_critical = 0
    

    if var_left > 0.17:
        valid_rot = 0
        valid_left = 0
        x_left = distance[(left_line/2) : (left_line/2 - 5)].min()
    else:
        valid_rot = 1
        valid_left = 1
        x_left = mean_left
        for i in range(left_line, 0):
            if distance[i] - mean_left > 10:
                left_critical = distance_angle[i]          #left line
                break

    if var_right > 0.17:
        valid_rot = 0 or valid_rot
        valid_right = 0
        x_right = distance[(right_line/2) : (right_line/2 + 5)].min()
    else:
        valid_rot = 1
        valid_right = 1
        x_right = mean_right
        for i in range(right_line, L):
            if distance[i] - mean_right > 10:
                right_critical = distance_angle[i]          #right line
                break

    if (x_left and x_right) >60:
        valid_rot = 0

    if valid_rot:
        if abs(e_angle) > 30:
            if e_angle > 0:
                m_angle = 150 - left_critical
            else:
                m_angle = 30 - right_critical
        else:
            if x_right > x_left:
                m_angle = 150 - left_critical
            else:
                m_angle = 30 - right_critical
    else:
        m_angle = e_angle

    centre_line = 90 - m_angle
    mean_centre = distance[centre_line + 10 : centre_line - 10].mean()
    var_centre = distance[centre_line + 10 : centre_line - 10].var()
    x_min = distance.min()

    if var_centre > 0.17:
        valid_centre = 0
        x_centre = distance[centre_line + 10 : centre_line - 10].min()
    else:
        valid_centre = 1
        x_centre = mean_centre                           #centre line

    z_t = np.array ([x_centre, x_left, x_right,  x_min, m_angle, valid_centre, valid_left, valid_right, valid_rot])

    return z_t

    
