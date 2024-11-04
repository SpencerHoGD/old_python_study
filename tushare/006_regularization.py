
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


ts.set_token('b6d2bad6b01d260afc0c48bac0b12975d4eb11aa99cf72b21bd19754')
pro = ts.pro_api()

hs300 = pro.index_daily(ts_code='399300.SZ', start_date='20190101', end_date='20190930')[['trade_date', 'pct_chg']]
df_000001 = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20190101', end_date='20190930')[['trade_date', 'pct_chg']]
df_000002 = ts.pro_bar(ts_code='000002.SZ', adj='qfq', start_date='20190101', end_date='20190930')[['trade_date', 'pct_chg']]
df = pd.merge(hs300, df_000001, df_000002, how='left', on='trade_date', sort=True, suffixes=['_hs300', '_000001', '_000002'])
df.iloc[:, 1:] = df.iloc[:, 1:] / 100
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
print(df.head())
print(df.info())