#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import numpy as np
import math
import random

def sensor_model (m_t0, s_t, z_t, c_angle):
    resolution = m_t0.get_resolution()
    _x_centre = 0
    _x_left = 0
    _x_right = 0

    if valid_centre:
        for m_ver in range (5, x_centre, resolution):
            for m_hor in range (- m_ver * np.tan(10), m_ver * np.tan(10), resolution):
                x_mi = x_t + m_ver * np.cos(c_angle) - m_hor * np.cos(c_angle + 90)   # x coordinate of grid cell
                y_mi = y_t + m_ver * np.sin(c_angle) - m_hor * np.sin(c_angle + 90)   # y coordinate of grid cell
                p_mi = m_t0. get_value(x_mi, y_mi)         #probability value at (x_mi, y_mi)
                if p_mi > 0.5:
                    _x_centre = m_ver
                    break
            if p_mi > 0.5:
                break
        if p_mi > 0.5:
            p_centre = random.gauss(abs(x_centre - _x_centre), 2)
        else:
            p_centre = 1
    else:
        p_centre = 1           #increase x_ver or _x_centre until find an occupied cell
                               #then take this x_ver as _x_centre

    if valid_left:
        for m_hor in range (5, x_left, resolution):
            for m_ver in range (- m_hor * np.tan(10), m_hor * np.tan(10), resolution):
                x_mi = x_t + m_hor * np.cos(c_angle + 90) - m_ver * np.cos(c_angle + 180)
                y_mi = y_t + m_hor * np.sin(c_angle + 90) - m_ver * np.sin(c_angle + 180)
                p_mi = m_t0. get_value(x_mi, y_mi)
                if p_mi > 0.5:
                    _x_left = m_hor
                    break
            if p_mi > 0.5:
                break
        if p_mi > 0.5:
            p_left = random.gauss(abs(x_left - _x_left), 2)
        else:
            p_left = 1
    else:
        p_left = 1

    if valid_right:
        for m_hor in range (5, x_right, resolution):
            for m_ver in range (- m_hor * np.tan(10), m_hor * np.tan(10), resolution):
                x_mi = x_t + m_hor * np.cos(c_angle - 90) - m_ver * np.cos(c_angle)
                y_mi = y_t + m_hor * np.sin(c_angle - 90) - m_ver * np.sin(c_angle)
                p_mi = m_t0. get_value(x_mi, y_mi)
                if p_mi > 0.5:
                    _x_right = m_hor
                    break
            if p_mi > 0.5:
                break
        if p_mi > 0.5:
            p_right = random.gauss(abs(x_right - _x_right), 2)
        else:
            p_right = 1
    else:
        p_right = 1

    if valid_rot:
        _m_angle = angle_t - c_angle
        p_rot = np.gauss(abs(m_angle - _m_angle), 3)
    else:
        p_rot = 1

    p_tot = p_rot * p_centre * p_left * p_right

    return p_tot