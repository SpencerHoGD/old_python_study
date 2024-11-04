from sqlalchemy import create_engine
import pandas as pd
import tushare as ts


ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
pro = ts.pro_api()
engine = create_engine('postgresql://postgres:394460@localhost:5432/postgres')
print('Database opened successfully')
code_list = ['000001.SZ', '000002.SZ']
for i in code_list:
    print(i)
    df = ts.pro_bar(ts_code=i, adj='qfq', start_date='20190601', end_date='20210823')
    df.to_sql(name='沪深股票qfq日线行情', con=engine, index=False, if_exists='append')


# df_index = pd.read_sql("SELECT ts_code, trade_date, close_p FROM 沪深300指数日线行情;", con=engine)
df_index = pd.read_sql("SELECT * FROM 沪深股票qfq日线行情;", con=engine)
print(df_index)
# print(df_index.head())