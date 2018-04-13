#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep
import numpy as np

def inverse_sensor_model(m_i, s_t, z_t, c_angle):

    angle_c_m = np.arctan2(y_mi - y_t, x_mi - x_t) - c_angle
    x_m = np.sqrt(np.square(y_mi - y_t) + np.square(x_mi - y_t))
    m_ver = abs(y_mi - y_t)
    m_hor = abs(x_mi - x_t)
    if x_m <= (x_min - 2) and angle_c_m <= 105 or angle_c_m >= 255:
        return 0.2
    elif (0 <= angle_c_m <= 20) or (340 <= angle_c_m < 360):
        if (0<= angle_c_m <= 10) or (350 <= angle_c_m < 360):
            if m_ver < (x_centre - 2):
                return 0.2
            elif ((x_centre + 2) >= m_ver >= (x_centre - 2)):
                if valid_centre == 1:
                    return 0.8
                else:
                    return 0.5
            else:
                return 0.5
        else:
            if m_ver < x_centre - 2:
                return 0.4
            elif ((x_centre + 2) >= m_ver >= (x_centre - 2)):
                if valid_centre == 1:
                    return 0.6
                else:
                    return 0.5
            else:
                return 0.5
    elif 70 <= angle_c_m <= 110:
        if 80 <= angle_c_m <= 100:
            if m_hor < (x_left - 2):
                return 0.2
            elif ((x_left + 2) >= m_hor >= (x_left - 2)):
                if valid_left == 1:
                    return 0.8
                else:
                    return 0.5
            else:
                return 0.5
        else:
            if m_hor < x_left - 2:
                return 0.4
            elif ((x_left + 2) >= m_hor >= (x_left - 2)):
                if valid_left == 1:
                    return 0.6
                else:
                    return 0.5
            else:
                return 0.5
    elif 250 <= angle_c_m <= 290:
        if 260 <= angle_c_m <= 280:
            if m_hor < (x_right - 2):
                return 0.2
            elif ((x_right + 2) >= m_hor >= (x_right - 2)):
                if valid_right == 1:
                    return 0.8
                else:
                    return 0.5
            else:
                return 0.5
        else:
            if m_hor < x_right - 2:
                return 0.4
            elif ((x_right + 2) >= m_hor >= (x_right - 2)):
                if valid_right == 1:
                    return 0.6
                else:
                    return 0.5
            else:
                return 0.5
    else:
        return 0.5
        
    
