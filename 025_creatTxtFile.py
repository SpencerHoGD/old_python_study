#!/usr/bin/env python3
# encoding:utf-8
'''
Created on 2019-08-01
'''
import os
#import time


def nsfile(s):
    '''The number of new expected documents'''
    # 判断文件夹是否存在，如果不存在则创建
    desdir = "/home/liam/test/testCreatFile/"
    b = os.path.exists(desdir)
    if b:
        print("Dir Exist!")
    else:
        os.mkdir(desdir)
   # #生成文件
   # print("请输入需要创建的txt文件个数")
   # s = input()

    for i in range(1, s+1):
        #    localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # print localtime
        filename = desdir + str(int(i)) + ".txt"
        #a:以追加模式打开（必要时可以创建）append; b:表示二进制
        with open(filename, 'a') as f:
            testnote = 'testnote\n'
            f.write(testnote)
            f.write(str(i))
        #输出第几个文件和对应的文件名称
        print(str(i)+".txt was written")
    #    time.sleep(1)
    print("ALL Done")
    # time.sleep(1)


if __name__ == '__main__':
    s = int(input("请输入需要生成的文件数："))
    nsfile(s)
