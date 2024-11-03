#! /usr/bin/env python
'''
Created on 2019-10-09
hexiaoming
'''

import os
from os import path
import datetime
import re


d = r'D:\work'  # 文件所在的文件夹路径
origin_file = path.join(d, 'Worklog1908-1912.md') # 制定目标文件
result_file = path.join(d, "short-content.md")   # 指定结果文件


if path.exists(result_file):
    print("file exists")
    os.remove(result_file)
    print("file has been removed")
else:
    print("file not exists")
    pass


regex = r"(#)(.*)(\s)(\d*)(/)(\d*)(/)(\d*)(.*)"

lines = open(origin_file, 'r', encoding='utf-8').readlines()

with open(result_file, 'w', encoding='utf-8') as f:  # 先创建打开结果文件
    for line in lines:
        mysearch = re.search(regex, line)
        if mysearch:
            month = mysearch.group(6)
            day = mysearch.group(8)
            title = mysearch.group(1) + mysearch.group(4) + mysearch.group(5) + mysearch.group(6) + mysearch.group(7) + mysearch.group(8) + mysearch.group(9)
            if day.startswith("01"):
                f.write('\n'*2 +  f'{month}' + '\n' + f'[{day}]({title})' + ' ')
            else:
                f.write(f'[{day}]({title})' + ' ')
    f.close


print("All done!")
