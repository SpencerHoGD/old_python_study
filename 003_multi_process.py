# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 求最大公约数

import cProfile

# import time
from concurrent.futures import Executor, ProcessPoolExecutor, ThreadPoolExecutor

from dectimeit import get_time


# 最大公约数
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [
    (19633090, 22659730),
    (18796750, 24936700),
    (20306770, 38141720),
    (15516450, 22296200),
    (19889120, 47366700),
    (21989640, 78762930),
]


# 不使用多线程/多进程
@get_time
def not_any():
    results = list(map(gcd, numbers))


# 多线程ThreadPoolExecutor
@get_time
def mulThread():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(gcd, numbers))


# 多进程ProcessPoolExecutor
@get_time
def mulProcess():
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(gcd, numbers))


if __name__ == "__main__":
    # not_any()
    # mulThread()
    # mulProcess()
    cProfile.run("mulProcess()")
