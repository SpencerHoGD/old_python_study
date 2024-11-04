import tushare as ts


pro = ts.pro_api('d70b0d73620a7853f31bad2ca374c144652d9200faff258cbf31254a')

# 拉取数据
df = pro.namechange(**{
    "ts_code": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "name",
    "start_date",
    "end_date",
    "ann_date",
    "change_reason"
])
print(df)
