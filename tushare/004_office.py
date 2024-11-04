import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np


pd.set_option("expand_frame_repr", False)       # 当列太多时不换行
plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号

# ts.set_token('b6d2bad6b01d260afc0c48bac0b12975d4eb11aa99cf72b21bd19754')
# pro = ts.pro_api()
pro = ts.pro_api('b6d2bad6b01d260afc0c48bac0b12975d4eb11aa99cf72b21bd19754')

# 导入000002.SZ前复权日线行情数据，保留收盘价列
df = ts.pro_bar(ts_code='002717.SZ', adj='qfq', start_date='20170101', end_date='20190930')
df.sort_values('trade_date', inplace=True)
df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
df = df[['close']]
# print(df.head())

# # 计算当前
# 、
# 未来1-day涨跌幅
df['1d_future_close'] = df['close'].shift(-1)
df['1d_close_future_pct'] = df['1d_future_close'].pct_change(1)
df['1d_close_pct'] = df['close'].pct_change(1)
df['ma5'] = df['close'].rolling(5).mean()
df['ma5_close_pct'] = df['ma5'].pct_change(1)
df.dropna(inplace=True)
feature_names = ['当前涨跌幅方向', 'ma5当前涨跌幅方向']

df.loc[df['1d_close_future_pct'] > 0, '未来1d涨跌幅方向'] = '上涨'
df.loc[df['1d_close_future_pct'] <= 0, '未来1d涨跌幅方向'] = '下跌'

df.loc[df['1d_close_pct'] > 0, '当前涨跌幅方向'] = 1    # 上涨记为1
df.loc[df['1d_close_pct'] <= 0, '当前涨跌幅方向'] = 0    # 下跌记为0

df.loc[df['ma5_close_pct'] > 0, 'ma5当前涨跌幅方向'] = 1
df.loc[df['ma5_close_pct'] <= 0, 'ma5当前涨跌幅方向'] = 0

feature_and_target_cols = ['未来1d涨跌幅方向'] + feature_names
df = df[feature_and_target_cols]
# print(df.head())
#            未来1d涨跌幅方向  当前涨跌幅方向  ma5当前涨跌幅方向
# trade_date
# 2019-01-09        下跌      1.0         1.0
# 2019-01-10        上涨      0.0         1.0
# 2019-01-11        下跌      1.0         1.0
# 2019-01-14        上涨      0.0         0.0
# 2019-01-15        上涨      1.0         1.0


# 创建特征 X 和标签 y
y = df['未来1d涨跌幅方向'].values
X = df.drop('未来1d涨跌幅方向', axis=1).values
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# 创建一个k为6的k-NN分类器
knn = KNeighborsClassifier(n_neighbors=6)
# 放入训练集数据进行学习
knn.fit(X_train, y_train)
# 在测试集数据上进行预测
new_prediction = knn.predict(X_test)
print("Prediction: {}".format(new_prediction))
# 测算模型的表现：预测对的个数 / 总个数
print(knn.score(X_test, y_test))

# Prediction: ['上涨' '下跌' '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '下跌' '上涨' '上涨' '上涨' '上涨' '上涨'
#  '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '上涨' '下跌' '下跌' '下跌' '上涨'
#  '上涨' '上涨' '上涨' '上涨' '下跌' '上涨' '下跌' '上涨']0.5555555555555556

# 上面的示例中用的是k=6，我们也可以尝试选取不同的k，再来看看预测的效果。

# 创建用于储存训练和测试集预测准确度的数组
neighbors = np.arange(1, 15)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))
# 循环输入不同的 k值
for i, k in enumerate(neighbors):
    # 构建knn分类器
    knn = KNeighborsClassifier(n_neighbors=k)
    # 用训练集数据学习
    knn.fit(X_train, y_train)
    # 计算在训练集数据上的准确度
    train_accuracy[i] = knn.score(X_train, y_train)
    # 计算在测试集数据上的准确度
    test_accuracy[i] = knn.score(X_test, y_test)
print(train_accuracy)
print(test_accuracy)
# 画图
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label='测试集预测准确度')
plt.plot(neighbors, train_accuracy, label='训练集预测准确度')
plt.legend()
plt.xlabel('k的取值')
plt.ylabel('准确度')
plt.show()
