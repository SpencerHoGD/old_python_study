#! /usr/bin/env python
'''
Created on 2019-10-12
hexiaoming
'''

import os
from os import path
import shutil
from shutil import copyfile



#需要查找复制的文件夹起始位置
srcDir = r'\\192.168.106.201\风控中心综合体系\07、文件模板、函件、通讯'
#想保存到的根路径
saveDir = r"D:\copy_file_from_NAS"
#如果目录不存在，则创建
if not path.isdir(saveDir):
    os.makedirs(saveDir)
        

def copy_file(srcDir):

    fileType = "pdf"
    counter = 0
    #nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #filelistlog = path.join("D:\\fileListLog" + str(nowTime) + ".txt")  # 保存文件路径)
    #postfix = set(['pdf','doc','docx','epub','txt','xlsx','djvu','chm','ppt','pptx'])  # 设置要保存的文件格式


    for maindir, subdir, file_name_list in os.walk(srcDir):
        for filename in file_name_list:
            from_path = os.path.join(maindir, filename)
            to_path = saveDir + "\\"
            # if True:        # 保存全部文件名。若要保留指定文件格式的文件名则注释该句
            if filename.split('.')[-1] == fileType:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                # 复制pdf文件
                shutil.copy2(from_path, to_path)
                counter += 1


    print(f'{count} {fileType} files has been copyed!')
        

if __name__ == '__main__':
    print('开始')
    copy_file(srcDir)
    print('完成')