import math

from dectimeit import get_time

# 23.58 seconds
# home windows 17.776 seconds
# Liam-arch 7.368 seconds
# Liam-arch use @get_time 4.145 seconds
# hxm-arch 4.933 s


@get_time
def test():
    for num in range(2, 2 * 10**6):
        is_prime = True
        for factor in range(2, int(math.floor(math.sqrt(num))) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            # print(num)
            pass


test()
