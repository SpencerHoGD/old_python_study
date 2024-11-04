import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
# import psycopg2
# import matplotlib.pyplot as plt


def connectPostgreSQL():
    db1 = 'hs_const'
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    # 获取沪股通成分
    df1 = pro.hs_const(hs_type='SH')

    # 获取深股通成分
    df2 = pro.hs_const(hs_type='SZ')

    print(df1)
    print(df2)

    engine = create_engine(
        'postgresql://postgres:394460@localhost:5432/postgres')
    print('connect successfully')
    df1.to_sql(name=db1, con=engine, index=False, if_exists='append')
    df2.to_sql(name=db1, con=engine, index=False, if_exists='append')


if __name__ == "__main__":
    connectPostgreSQL()
