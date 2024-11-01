#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-06
hexiaoming
'''

import matplotlib.pyplot as plt
from os import path


d = path.dirname(__file__)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#plt.savefig(path.join(d, "matplotlib_bingtu.png"))
