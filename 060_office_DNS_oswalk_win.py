#! /usr/bin/env python
'''
Created on 2019-10-10
hexiaoming
'''


import os
from os import path
import datetime


#d = r'\\192.168.106.201\风控中心综合体系\09、资金计划、报销、福利、资产管理'
#os.system("explorer.exe %s" % d)
#os.startfile(path)
#os.system('notepad')

#fileList = os.listdir(d)

#print(fileList)

def all_path(startDir):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filelistlog = path.join("D:\\fileListLog" + str(nowTime) + ".txt")  # 保存文件路径)
    postfix = set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式
    for maindir, subdir, file_name_list in os.walk(startDir):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
            #if apath.split('.')[-1] in postfix:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                try:
                    with open(filelistlog, 'a+', encoding='utf8') as fo:
                        fo.writelines(apath)
                        fo.write('\n')
                    fo.close
                except:
                    pass    # 所有异常全部忽略即可

    
if __name__ == '__main__':
    startDir = "E:"  # 指定根目录
    #startDir = r'\\192.168.106.201\风控中心综合体系'
    #startDir  = r'\\192.168.106.201\风控中心\监察部'  #监察部共享
    #startDir  = r'\\192.168.106.201\风控中心\审计部'  #审计部共享
    print('开始')
    all_path(startDir)
    print('完成')