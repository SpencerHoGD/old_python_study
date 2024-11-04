import psycopg2
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
# from sqlalchemy import create_engine


def selectOperate():
    db1 = 'daily'
    stock_code = '002717.SZ'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port='5432')

    QL1 = "select * from {};".format(db1)
    QL2 = "SELECT ts_code, trade_date, close_p FROM {};".format(db1)
    QL3 = "select * from {} where trade_date between \
           '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    QL4 = "select ts_code, trade_date, close_p from {} where trade_date between \
           '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    QL5 = "select trade_date, close_p from {} where ts_code = '{}' \
           ORDER BY trade_date ASC".format(db1, stock_code)
    QL6 = "select trade_date from {} \
           ORDER BY trade_date ASC".format(db1)
    QL7 = "select ts_code, trade_date, close_p from {} where trade_date between \
           '2017-12-27' and '2017-12-28';".format(db1)

    df = pd.read_sql(SQL7, con=conn)
    print(df.tail())

#     df.sort_values('trade_date', inplace=True)
#     df.reset_index(inplace=True, drop=True)
    # print(df.head())
#     print(df.dtypes)
#     print(df.shape)

#     df.set_index('trade_date', inplace=True)

#     ax = df.plot(color='blue', figsize=(8, 3), linewidth=2, fontsize=6)
#     ax.set_title('002717.SZ close from 2014-02-14 to 2019-12-13', fontsize=8)
#     ax.set_xlabel('trade_date')
#     ax.set_ylabel('002717.SZ close')
#     ax.axvline('2019-01-01', color='red', linestyle='--')
#     ax.axhline(8.9, color='green', linestyle='--')
#     plt.show()

#     ma = df.rolling(window=250).mean()
#     mstd = df.rolling(window=250).std()
#     ma['upper'] = ma['close_p'] + (mstd['close_p'] * 2)
#     ma['lower'] = ma['close_p'] - (mstd['close_p'] * 2)
#     ax = ma.plot(linewidth=0.8, fontsize=6)

#     plt.show()

    conn.close()


if __name__ == "__main__":
    selectOperate()
