import psycopg2 
import pandas as pd 
import tushare as ts 
# from sqlalchemy import create_engine 


def connectPostgreSQL():
    db = 'daily'
    conn = psycopg2.connect(database='testdb', user='postgres', \
        password='394460', host='127.0.0.1', port=5432)
    print('connect successful!')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE {}
                                      (ts_code          VARCHAR(10)      NOT NULL,
                                       trade_date       DATE             NOT NULL,
                                       open_p           NUMERIC          DEFAULT 0,
                                       high_p           NUMERIC          DEFAULT 0,
                                       low_p            NUMERIC          DEFAULT 0,
                                       close_p          NUMERIC          DEFAULT 0,
                                       pre_close        NUMERIC          DEFAULT 0,
                                       change           NUMERIC          DEFAULT 0,
                                       pct_chg          NUMERIC          DEFAULT 0,
                                       vol              NUMERIC          DEFAULT 0,
                                       amount           NUMERIC          DEFAULT 0,
                                       PRIMARY KEY (ts_code, trade_date)
                                        );""".format(db))
    conn.commit()
    conn.close()
    print('table {} is created!'.format(db))


def insertOperate():
    db = 'daily'
    ts.set_token('74eabb1fce9fd5c317fd38477a465d0aa4eb167e0ee272be91631a0e')
    pro = ts.pro_api()

    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')

    df = pro.daily(trade_date = '20191129')

    ts_code    = df['ts_code'].tolist()
    trade_date = df['trade_date'].tolist()
    open_p     = df['open'].tolist()
    high_p     = df['high'].tolist()
    low_p      = df['low'].tolist()
    close_p    = df['close'].tolist()
    pre_close  = df['pre_close'].tolist()
    change     = df['change'].tolist()
    pct_chg    = df['pct_chg'].tolist()
    vol        = df['vol'].tolist()
    amount     = df['amount'].tolist()
    
    count = 0
    for i in range(len(ts_code)):
        cursor.execute("""INSERT INTO daily
        (ts_code, trade_date, open_p, high_p, low_p, close_p,
         pre_close, change, pct_chg, vol, amount)
        VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                     (ts_code[i],
                      trade_date[i],
                      open_p[i],
                      high_p[i],
                      low_p[i],
                      close_p[i],
                      pre_close[i],
                      change[i],
                      pct_chg[i],
                      vol[i],
                      amount[i]))
        conn.commit()
        count += 1 

    conn.close()
    print('insert {}th of {} records at {} into table "{}" successfully'.format(count, len(ts_code), trade_date[0], db))



def selectOperate():
    db = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    # cursor.execute("select * from {}".format(db))
    cursor.execute("select * from {}".format(db))
    rows = cursor.fetchall()
    # print(len(rows))
    for row in rows[-10:]:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    conn.close()



def selectOperate1():
    db = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    # cursor.execute("select * from {} where trade_date between '2019-11-29 00:00:00' and '2019-11-29 23:59:59' ".format(db))
    cursor.execute("select * from {} ".format(db))
    rows = cursor.fetchall()
    # print(len(rows))
    for row in rows[:10]:
        print(row)
    conn.close()


def deleteOperate():
    db = 'daily'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    cursor.execute("delete from {} where trade_date between \
        '2019-11-29 00:00:00' and '2019-11-29 23:59:59' ".format(db))
    conn.commit()   
    print('end delete')
    print("Total number of rows deleted :", cursor.rowcount)
    conn.close()

if __name__ == "__main__":
    connectPostgreSQL()
    # insertOperate()
    # selectOperate()
    # selectOperate1()
    # deleteOperate()
