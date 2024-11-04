import psycopg2
import pandas as pd
import tushare as ts
# from sqlalchemy import create_engine


def selectOperate():
    db1 = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    # cursor.execute("select * from {}".format(db1))
    cursor.execute("select * from {} where trade_date between \
        '2017-12-27 00:00:00' and '2017-12-28 23:59:59' ".format(db1))
    rows = cursor.fetchall()
    print(len(rows))
    # for row in rows[-10:]:
    # for row in rows[:10]:
    #     print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], \
    #           row[7], row[8], row[9], row[10])
    conn.close()


def selectOperate1():
    db1 = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port='5432')

    SQL1 = "select * from {};".format(db1)
    SQL2 = "SELECT ts_code, trade_date, close_p FROM {};".format(db1)
    SQL3 = "select * from {} where trade_date between \
            '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    SQL4 = "select ts_code, trade_date, close_p from {} where trade_date between \
            '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)

    df_index = pd.read_sql(SQL4, con=conn)
    print(df_index.head())

    with conn:
        with conn.cursor() as curs:
            curs.execute(SQL2)
            rows = curs.fetchall()
            # print(len(rows))
            # for row in rows[-10:]:
            for row in rows[:10]:
                print(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                      row[7], row[8], row[9], row[10])
    conn.close()


def selectOperate2():
    db1 = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port='5432')

    SQL1 = "select * from {};".format(db1)
    SQL2 = "SELECT ts_code, trade_date, close_p FROM {};".format(db1)
    SQL3 = "select * from {} where trade_date between \
            '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    SQL4 = "select ts_code, trade_date, close_p from {} where trade_date between \
            '2017-12-27 00:00:00' and '2017-12-28 23:59:59';".format(db1)
    SQL5 = "select ts_code, trade_date, close_p, amount from {} where trade_date = '2021-08-24';".format(db1)
    SQL6 = "select * from {} where trade_date = '2021-08-24' ORDER BY ts_code ASC;".format(db1)

    df_index = pd.read_sql(SQL6, con=conn)
    # df_index.to_csv('daily_20210824.csv')
    print(df_index.head())

    conn.close()


if __name__ == "__main__":
    # selectOperate()
    # selectOperate1()
    selectOperate2()
