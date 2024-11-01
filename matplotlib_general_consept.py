#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-06
hexiaoming
'''

import matplotlib.pyplot as plt
import numpy as np


# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
#
# plt.xlabel('x label')
# plt.ylabel('y label')
#
# plt.title("Simple Plot")
#
# plt.legend()
#
# plt.show()

# x = np.arange(0, 10, 0.01)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# def my_plotter(ax, data1, data2, param_dict):
#    """
#    A helper function to make a graph
#
#    Parameters
#    ----------
#    ax : Axes
#        The axes to draw to

    data1: array
       The x data

    data2: array
       The y data

    param_dict: dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out: list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

plt.show()
