import ev3dev.ev3 as ev3
from time import sleep
import numpy as np
import math
import random
import matplotlib.pyplot as plt

def sample_motion_model(s_t0 = np.array([0, 0, 0]), u = np.array([0, 0, 0])):
    x_t0, y_t0, angle_t0 = s_t0[0], s_t0[1], s_t0[2]
    rot1, trans1, rot2 = u[0], u[1], u[2]

    _rot1 = rot1 + random.uniform(-(0.008*abs(rot1) + 0.0008*abs(trans1)),(0.008*abs(rot1) + 0.0008*abs(trans1)))
    _trans1 = trans1 + random.uniform((-0.034*(abs(rot1) + abs(rot2)) + 0.0023*abs(trans1)),(0.034*(abs(rot1) + abs(rot2)) + 0.0023*abs(trans1)))
    _rot2 = rot2 + random.uniform(-(0.008*abs(rot2) + 0.0008*abs(trans1)),(0.008*abs(rot2) + 0.0008*abs(trans1)))

    x_t = round(x_t0 + _trans1 * math.cos(math.radians(angle_t0 + _rot1)),3)
    y_t = round(y_t0 + _trans1 * math.sin(math.radians(angle_t0 + _rot1)),3)
    angle_t = int(angle_t0 + _rot1 + _rot2)

    s_t = np.array([x_t, y_t, angle_t])

    return s_t

#s = sample_motion_model(s_t0 = np.array([0, 0, 0]), u = np.array([45, 20, -45]))
#print(s)

plt.figure(figsize=(80, 10), dpi=80)
plt.xlim(0, 18)
plt.ylim(0, 18)

plt.arrow(0,0,14.14,14.14,width=0.01, color = 'red')
for i in range(0, 500):
    s = sample_motion_model(s_t0 = np.array([0, 0, 0]), u = np.array([45, 20, -45]))
    plt.scatter(s[0], s[1], s=100, c='blue', marker='.', alpha=None, edgecolors='white')
    plt.legend()
plt.show()


