#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-04
hexiaoming
'''
import numpy as np
import pandas as pd
import string

rng = pd.date_range('10/4/2019', periods=100, freq='Min')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
rts = ts.resample('10Min').sum()
print(rts)
