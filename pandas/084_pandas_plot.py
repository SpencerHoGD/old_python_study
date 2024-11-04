#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-04
hexiaoming
'''
import numpy as np
import pandas as pd
import os
from os import path
import matplotlib.pyplot as plt

plt.close('all')

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))


ts = ts.cumsum()

ts.plot()
