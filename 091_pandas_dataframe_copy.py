#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-05
hexiaoming
'''
import numpy as np
import pandas as pd
import string
import os
from os import path

d = path.dirname(__file__)
#dfd = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

#dfd['date'] = pd.Timestamp('20191005')

#dfd = dfd.sort_index(1, ascending=False)

#json = dfd.to_json(date_format='iso')
#json = dfd.to_json(date_format='iso', date_unit='us')
#json = dfd.to_json(date_format='epoch', date_unit='s')

df = pd.DataFrame(np.random.randn(10, 4))
df.to_excel(path.join(d, 'pandas_dataframe_XLSX.xlsx'))

r = pd.read_excel(path.join(d, 'pandas_dataframe_XLSX.xlsx'))
print(r)

os.remove(path.join(d, 'pandas_dataframe_XLSX.xlsx'))

