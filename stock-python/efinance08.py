# 导入 efinance 如果没有安装则需要通过执行命令: pip install efinance 来安装
# 获取最新季报
import efinance as ef
# 股票名称
filenane = 'realtime_quotes'
df14 = ef.stock.get_realtime_quotes()   # 获取沪深市场最新行情总体情况
# 将数据存储到 csv 文件中
df14.to_csv(f'{filenane}.csv', encoding='utf-8-sig', index=None)
print(f'股票: {filenane} 的行情数据已存储到文件: {filenane}.csv 中！')