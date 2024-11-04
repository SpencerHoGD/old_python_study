import tushare as ts


pro = ts.pro_api('b6d2bad6b01d260afc0c48bac0b12975d4eb11aa99cf72b21bd19754')

# df = pro.query('trade_cal', exchange='', start_date='20191001', end_date='20191208', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

# df = ts.get_today_all()
# df1 = ts.get_hist_data('002717')
df2 = pro.daily(ts_code='002717.SZ',
                start_date='20210801', end_date='202r0824')


# data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(data)

# df1.head(100)
print(df2.head(100))
