import os
from os import path
from itertools import islice


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


# dst = './tmp/gennerator_fib.txt'
dst = '~/test/gennerator_fib.txt'
if path.exists(dst):
    print("dst file exists!")
    os.remove(dst)
    print("dst file removed!")
else:
    print("dst file not exists!")
    pass


f = fib()
fib_list = list(islice(f, 0, 100))
with open(dst, 'w') as dstf:
    for i in fib_list:
        dstf.write(str(i) + '\n')
    print("fib list writtened!")

print("Done")
