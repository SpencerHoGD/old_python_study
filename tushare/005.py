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


pd.set_option("expand_frame_repr", False)       # 当列太多时不换行
plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号

ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
pro = ts.pro_api()


hs300 = pro.index_daily(ts_code='399300.SZ', start_date='20190101', end_date='20190930')[['trade_date', 'pct_chg']]
df_000001 = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20190101', end_date='20190930')[['trade_date', 'pct_chg']]
df = pd.merge(hs300, df_000001, how='left', on='trade_date', sort=True, suffixes=['_hs300', '_000001'])
df.iloc[:, 1:] = df.iloc[:, 1:] / 100
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
# print(df.head())
# print(df.info())


# 画图：查看相关性
# plt.figure()
# sns.heatmap(df.corr(), annot=True, square=True, cmap='RdYlGn')
# plt.show()


# 从sklearn.linear_model模块调用LinearRegression类做线性回归。
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 创建线性回归模型
reg_all = LinearRegression()
# 用训练集数据学习
reg_all.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = reg_all.predict(X_test)
# 计算评价指标R^2：
# print("R^2: {}".format(reg_all.score(X_test, y_test)))


# 调用sklearn.model_selection模块中的cross_val_score方法实现这一功能。
reg = LinearRegression()
# 计算k折交叉验证得分：以k=5为例
cv_scores = cross_val_score(reg, X, y, cv=5)
print(cv_scores)
print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))