import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
# import psycopg2
# import matplotlib.pyplot as plt


def connectPostgreSQL():
    db1 = 'new_share'
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    year1 = 2010
    year2 = 2019
    start_date = '{}0101'.format(year1)
    end_date = '{}1231'.format(year2)
    df = pro.new_share(start_date=start_date, end_date=end_date)

    engine = create_engine(
        'postgresql://postgres:394460@localhost:5432/postgres')
    print('connect successfully')
    df.to_sql(name=db1, con=engine, index=False, if_exists='append')


if __name__ == "__main__":
    connectPostgreSQL()
