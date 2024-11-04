# 导入 efinance 如果没有安装则需要通过执行命令: pip install efinance 来安装
# 根据股票代码获取最新第一个交易日的分钟数据
import efinance as ef

df10 = ef.stock.get_base_info()    # 股票代码或股票代码结构的列表
df11 = ef.stock.get_history_bill()    # 单只股票历史单子流入流出的数据
df12 = ef.stock.get_latest_quote()    # 沪深多只股票实时涨跌幅情况
df13 = ef.stock.get_quote_history()    # 获取股票、债券、etf的k线数据
df14 = ef.stock.get_realtime_quotes()    # 获取沪深市场最新行情总体情况
df15 = ef.stock.get_today_bill()    # 最新单只股票流入流出的数据
df16 = ef.stock.get_top10_stock_holder_info()    # 沪深市场指定股票前十大股东信息

df20 = ef.fund.get_base_info()    # 
df21 = ef.fund.get_fund_codes()    # 
df22 = ef.fund.get_industry_distribution()    # 
df23 = ef.fund.get_inverst_position()    # 
df24 = ef.fund.get_pdf_reports()    # 
df25 = ef.fund.get_public_dates()    # 
df26 = ef.fund.get_period_change()    # 
df27 = ef.fund.get_quote_history()    # 
df28 = ef.fund.get_realtime_increase_rate()    # 
df29 = ef.fund.get_types_persentage()    # 

df30 = ef.bond.get_all_base_info()    # 
df31 = ef.bond.get_base_info()    # 
df32 = ef.bond.get_quote_history()    # 
df33 = ef.bond.get_realtime_quotes()    # 

df40 = ef.futures.get_futures_base_info()    # 
df41 = ef.futures.get_quote_history()    #获取期货历史行情信息