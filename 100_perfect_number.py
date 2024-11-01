"""
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）
的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数

Version: 0.1
Author: hxm
home win:10000,3.983sec
home liam-arch:10000,1.972sec
home liam-arch:10000,@get-time 1.306sec
"""


# import time
from dectimeit import get_time


# start = time.time()
@get_time
def t():
    for i in range(1, 1*10**4):
        num = 0
        for k in range(1, i):
            if i % k == 0:
                num += k
        if i == num:
            print(i)

# end = time.time()
# print('Took %.3f seconds.' % (end - start))
t()    
