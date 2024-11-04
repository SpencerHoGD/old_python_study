import os 
import sys 
import psycopg2 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine 


def connectPostgreSQL():
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    print('connect successful!')
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE 沪深300指数日线行情
                                      (ts_code          VARCHAR(10)      NOT NULL,
                                       trade_date       DATE             NOT NULL,
                                       open_p           NUMERIC          DEFAULT 0,
                                       high_p           NUMERIC          DEFAULT 0,
                                       low_p            NUMERIC          DEFAULT 0,
                                       close_p          NUMERIC          DEFAULT 0,
                                       pre_close        NUMERIC          DEFAULT 0,
                                       pct_chg          NUMERIC          DEFAULT 0,
                                       PRIMARY KEY (ts_code, trade_date)
                                        );""")
    conn.commit()
    conn.close()
    print('table 沪深300指数日线行情 is created!')


def insertOperate():
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()


    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')

    # 单位：涨跌幅（%）, 成交量（手）、成交额（千元）
    df = pro.index_daily(ts_code='399300.SZ', start_date='20210101', end_date='20210823')
    ts_code = df['ts_code'].tolist()
    trade_date = df['trade_date'].tolist()
    open_p = df['open'].tolist()
    high_p = df['high'].tolist()
    low_p = df['low'].tolist()
    close_p = df['close'].tolist()
    pre_close = df['pre_close'].tolist()
    pct_chg = df['pct_chg'].tolist()
    count = 0
    for i in range(len(ts_code)):
        cursor.execute("""INSERT INTO 沪深300指数日线行情 
        (ts_code, trade_date, open_p, high_p, low_p, close_p, pre_close, pct_chg)
        VALUES( %s, %s, %s, %s, %s, %s, %s, %s);""",
                     (ts_code[i],
                      trade_date[i],
                      open_p[i],
                      high_p[i],
                      low_p[i],
                      close_p[i],
                      pre_close[i],
                      pct_chg[i]))
        conn.commit()
        print("已插入第{0}行，共有{1}行".format(count, len(ts_code)))
        count += 1 

    conn.close()
    print('insert records into 沪深300指数日线行情 successfully')


def selectOperate():
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')
    cursor.execute("select * from 沪深300指数日线行情")
    rows = cursor.fetchall()
    for row in rows:
        print('id=', row[0], ',name=', row[1], ',pwd=',row[2], ',singal=', row[3], '\n')
        print(row)
    conn.close()



def deleteOperate():
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')

    print('begin delete')
    cursor.execute("delete from public.member where id=4")
    conn.commit()   
    print('end delete')
    print("Total number of rows deleted :", cursor.rowcount)
    
    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    conn.close()




if __name__ == "__main__":
    # connectPostgreSQL()
    insertOperate()
    # selectOperate()
    # updateOperate()
    # deleteOperate()
