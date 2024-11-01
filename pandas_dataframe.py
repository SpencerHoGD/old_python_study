#! /usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-10-04
hexiaoming
'''
import numpy as np
import pandas as pd
import string
import os
from os import path
import urllib

d = path.dirname(__file__)
index_num = 52
half_num = index_num // 2
col_num = list(string.ascii_uppercase)[:half_num]
word1 = '\n Hello world! \n'

dates = pd.date_range('20210701', periods=index_num, freq='H')
df = pd.DataFrame(np.random.randn(index_num, half_num),
                  index=dates, columns=col_num)

result = df

result = df.sort_values(by='B')
result = df.sort_index(axis=1, ascending=False)
result = df[0:3]
result = df.T
result = df.describe()
result = df.to_numpy()
result = df.head()
result = df.tail()

result = df.loc[dates[0]]
result = df.loc[:, ['A', 'B']]
result = df.loc['20191004':'20191007', ['A', 'B']]
result = df.loc[dates[0], 'A']
result = df.at[dates[0], 'A']
result = df.iloc[3:5, 0:2]
result = df.iloc[3:5, :]
result = df.iloc[[1, 2, 4], [0, 2]]
result = df[df.A > 0]
result = df[df > 0]
result.to_csv(path.join(d, 'pandas_dataframe_csv.csv'))
result.to_excel(path.join(d, 'pandas_dataframe_excel.xls'))
print(result)
