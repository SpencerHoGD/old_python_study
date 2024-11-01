#coding:utf-8
#author:hexiaoming
'''
Created on 2019-08-01
'''

import os

path = "D:/rename"
filelist =  os.listdir(path)
textfilename = "D:/rename/filedir_list.txt"
count = 0

for file in filelist:
    with open(textfilename, 'a') as f:
        f.write(str(count).zfill(4) + ',' + file + '\n')
        count += 1

        
print('success')


