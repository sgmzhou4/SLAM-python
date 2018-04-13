#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep
import numpy as np


def particle_filter(particle_t0, u_t, z_t):
    _particle_t = weight_t = []
    for i in range(1, N):
