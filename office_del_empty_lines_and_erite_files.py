'''
复制某个.md文档，删掉里面的空行
Created on 2019-10-09
hexiaoming
'''

import os
from os import path
import datetime
import re

d = r'D:\Read_Write'  # 文件所在的文件夹路径
origin_file = path.join(d, '浅谈岭南园林的利润获得.md') # 制定目标文件
result_file = path.join(d, '浅谈岭南园林的利润获得删空行.md')   # 指定结果文件

regex = r"^[ \t]*\n"

lines = open(origin_file, 'r', encoding='utf-8').readlines()

with open(result_file, 'w', encoding='utf-8') as f:  # 先创建打开结果文件
    for line in lines:
        mysearch = re.search(regex, line)
        if not mysearch:
            f.write(line)

print("All done!")