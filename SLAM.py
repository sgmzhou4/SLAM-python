#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep
import numpy as np

def SLAM (pose_t0, map_t0, n_l, n_r, distance, distance_angle):
    s_t = w_t = map_t = []
    u_t = odometry_data_filter(n_l, n_r)
    for i in range (0, N):
        s_t0[i] = pose_t0[i]
        m_t0[i] = map_t0[i]
        _s_t[i] =
