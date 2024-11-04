import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('expand_frame_repr', False)  # 显示所有列
ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
pro = ts.pro_api()


df = pro.index_daily(ts_code='399300.SZ')[['trade_date', 'close']]
df.sort_values('trade_date', inplace=True)
df.reset_index(inplace=True, drop=True)
# print(df.head())
# print(df.dtypes)

df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)
# print(df.head())


ax = df.plot(color='blue')
ax.set_xlabel('trade_date')
ax.set_ylabel('399300SZ close')
plt.show()
