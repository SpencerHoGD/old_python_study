import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import cross_val_score


pro = ts.pro_api('b6d2bad6b01d260afc0c48bac0b12975d4eb11aa99cf72b21bd19754')

hs300 = pro.index_daily(ts_code='399300.SZ', start_date='20190101',
                        end_date='20190930')[['trade_date', 'pct_chg']]
df_000001 = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20190101',
                       end_date='20190930')[['trade_date', 'pct_chg']]
df = pd.merge(hs300, df_000001, how='left', on='trade_date',
              sort=True, suffixes=['_hs300', '_000001'])
df.iloc[:, 1:] = df.iloc[:, 1:] / 100
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
# df.to_csv('hs300_000001.csv')
# print(df.head())
# print(df.info())

# 画图：查看相关性
# plt.figure()
# sns.heatmap(df.corr(), annot=True, square=True, cmap='RdYlGn')
# plt.show()

# 创建特征和标签
y = df['pct_chg_hs300'].values
X = df['pct_chg_000001'].values
print("转换前y的维度: {}".format(y.shape))
print("转换前X的维度: {}".format(X.shape))
# 转换成 n × 1维数组
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
print("转换后y的维度: {}".format(y.shape))
print("转换后X的维度: {}".format(X.shape))
# 创建训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
# 创建线性回归模型
reg_all = LinearRegression()
# 用训练集数据学习
reg_all.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = reg_all.predict(X_test)
# 计算评价指标R^2：
# print("R^2: {}".format(reg_all.score(X_test, y_test)))


reg = LinearRegression()
# 计算k折交叉验证得分：以k=5为例
cv_scores = cross_val_score(reg, X, y, cv=5)
print(cv_scores)
print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
