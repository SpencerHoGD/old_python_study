import psycopg2
import pandas as pd
import tushare as ts
import datetime
# from sqlalchemy import create_engine


def download_daily_today():
    today = datetime.date.today()

    conn = psycopg2.connect(database='postgres', user='postgres',
                            password='394460', host='127.0.0.1', port=5432)
    cursor = conn.cursor()
    print('connect successful!')

    ts.set_token('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')
    pro = ts.pro_api()

    df = pro.daily(trade_date='{}'.format(today))
    print(df.head())


    ts_code = df['ts_code'].tolist()
    trade_date = df['trade_date'].tolist()
    open_p = df['open'].tolist()
    high_p = df['high'].tolist()
    low_p = df['low'].tolist()
    close_p = df['close'].tolist()
    pre_close = df['pre_close'].tolist()
    change = df['change'].tolist()
    pct_chg = df['pct_chg'].tolist()
    vol = df['vol'].tolist()
    amount = df['amount'].tolist()

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
    print('insert records into table successfully')



if __name__ == "__main__":
    download_daily_today()
