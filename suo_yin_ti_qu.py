#coding:utf-8
#author:hexiaoming
'''
Created on 2019-09-09
'''


import random
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

print()
# 根据索引提取（Slicing）
print(c_list[3])        # 返回索引值为 3 的元素值
print(c_list[:])        # 相当于 c_list，返回整个列表
print(c_list[5:])       # 从索引为 5 的值开始直到末尾
print(c_list[:3])       # 从索引 0 开始，直到索引 3 之前（不包括 3）
print(c_list[2:6])      # 从索引 2 开始，直到索引 6 之前（不包括 6）

print()
# 根据索引删除
del c_list[3]
print(c_list)           # del 是个命令，del c_list[3] 是一个语句；不能这么写：print(del c_list[3])
del c_list[5:8]
print(c_list)

print()
# 根据索引替换
c_list[1:5:2] = ['a', 2]  # s[start:stop:step] = t，跟 range 的三个参数类似；

print(c_list)