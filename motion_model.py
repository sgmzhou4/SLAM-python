import ev3dev.ev3 as ev3
from time import sleep
import numpy as np
import math
import random

def motion_model(s_t0 = np.array([]), s_t = np.array([]), u = np.array([])):
    x_t0, y_t0, angle_t0 = s_t0[0], s_t0[1], s_t0[2] #s(t-1)
    x_t, y_t, angle_t = s_t[0], s_t[1], s_t[2] #s(t)
    rot1, trans1, rot2 = u[0], u[1], u[2] #u(t)

    _x_t = x_t0 + trans1*math.cos(math.radians(angle_t0 + rot1))
    _y_t = y_t0 + trans1*math.sin(math.radians(angle_t0 + rot1))
    _angle_t = angle_t0 + rot1 + rot2          #transition pose

    rot_start = math.degrees(math.atan2(y_t - y_t0, x_t - x_t0) - angle_t0)
    rot_end = angle_t - angle_t0 - rot_start
    trans = np.sqrt(np.square(y_t-y_t0) + np.square(x_t-x_t0))    #expected

    _rot_start = math.degrees(math.atan2(_y_t - y_t0, _x_t - x_t0) - angle_t0)
    _rot_end = _angle_t - angle_t0 - _rot_start
    _trans = np.sqrt(np.square(_y_t-y_t0) + np.square(_x_t-x_t0))   #real

    p1 = random.gauss(abs(rot_start - _rot_start) , 0.008*abs(rot_start) + 0.0008*abs(trans))
    p2 = random.gauss(abs(trans - _trans) , 0.034*(abs(rot_end) + abs(rot_start)) + 0.0023*abs(trans))
    p3 = random.gauss(abs(rot_end - _rot_end) , 0.008*abs(rot_end) + 0.0008*abs(trans))  #probability

    p_motion = p1*p2*p3

    print(float(p_motion))
    print(rot_start)
    print(rot_end)
    print(_rot_start)
    print(_rot_end)
    print(_x_t)
    print(_y_t)
    print(trans)
    print(_trans)
    print(p1)
    print(p2)
    print(p3)


motion_model(s_t0 = np.array([0, 0, 0]), s_t = np.array([1, 1, 0]), u = np.array([45, 2, -45]))