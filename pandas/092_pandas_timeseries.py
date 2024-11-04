#! /usr/bin/env python3
# encoding:utf-8
"""
Created on 2019-10-04
Modifiy on 2024-11-04
hexiaoming
"""

import numpy as np
import pandas as pd

P = 60 * 24
rng = pd.date_range("11/4/2024", periods=P, freq="Min")
ts = pd.Series(np.random.randint(0, 999, len(rng)), index=rng)
print(ts)

# rts = ts.resample("10Min").sum()
# print(rts)
