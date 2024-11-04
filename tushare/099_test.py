import psycopg2 
import pandas as pd 
import tushare as ts 
from sqlalchemy import create_engine 


def test0():
    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')

    # df = pro.stock_basic(exchange='', list_status='L')
    # df = pro.query('trade_cal', start_date='20000101', end_date='20191231')
    # df = pro.daily(trade_date = '20191211')
    # df1 = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    df1 = pro.stock_basic(exchange='', list_status='L')
    # df2 = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # df2 = pro.query('stock_basic', exchange='', list_status='L')
    # print(df.head(20))
    # print(df['exchange'].head())
    print(df1.tail())
    # print(df2.tail())

    # ts_code = df['ts_code'].tolist()
    # ts_symbol = df['symbol'].tolist()
    # ts_name = df['name'].tolist()
    # ts_area = df['area'].tolist()
    # ts_industry = df['industry'].tolist()
    # ts_market = df['market'].tolist()
    # ts_list_date = df['list_date'].tolist()
    # count = 0
    # for i in range(len(ts_code)):
    #     cursor.execute("""INSERT INTO stock_basic
    #     (ts_code, ts_symbol, ts_name, ts_area, ts_industry, ts_market, ts_list_date)
    #     VALUES( %s, %s, %s, %s, %s, %s, %s);""",
    #                  (ts_code[i],
    #                   ts_symbol[i],
    #                   ts_name[i],
    #                   ts_area[i],
    #                   ts_industry[i],
    #                   ts_market[i],
    #                   ts_list_date[i]))
    #     conn.commit()
    #     print("已插入第{0}行，共有{1}行".format(count, len(ts_code)))
    #     count += 1 

    conn.close()
    print('insert records into stock_basic successfully')



def test_print_head():
    db1 = 'stock_basic'
    conn = psycopg2.connect(database='postgres', user='postgres', password='394460', host='127.0.0.1', port=5432)
    cursor=conn.cursor()
    print('connect successful!')
    cursor.execute("select * from {}".format(db1))
    rows = cursor.fetchall()
    for row in rows[-10:]:
        print(row)
    conn.close()




if __name__ == "__main__":
    test0()
    # test_print_head()