import math

from dectimeit import get_time

# 7.7 seconds
# 2.272 sec lian-arch
# arch-hxm: 2.671 seconds
# arch-hxm: 73.671 seconds


# @get_time
def is_prime(n):
    """yes"""
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@get_time
def normal(n):
    """yes"""
    for num in range(2, n):
        if is_prime(num):
            pass


if __name__ == "__main__":
    N = 2 * 10**7
    normal(N)
