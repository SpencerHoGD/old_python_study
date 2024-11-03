#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-05
hexiaoming
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from os import path

d = path.dirname(__file__)

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig(path.join(d, "simple_plot_sin.png"))
# plt.show()
