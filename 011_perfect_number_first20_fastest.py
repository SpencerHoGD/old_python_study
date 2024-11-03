import datetime

# Python实现，由于Python底层运算直接用C或C+++实现所以比Java运算快一些
# arch-hxm: 27.10 total_seconds


def is_prime(n):
    """isprime"""
    if n < 4:
        return n > 1
    if (n & 1) == 0:
        return False
    i = 3
    while i * i <= n:
        if (n % i) == 0:
            return False
        i += 2
    return True


def primality(n, m):
    """primality"""
    if n == 2:
        return True
    s = 4
    for _ in range(0, n - 2):
        s = (s * s - 2) % m
    return s == 0


def find_perfect_number():
    """find_perfect_number"""
    count = 0
    begin = datetime.datetime.now()
    str_content = ""
    for i in range(2, 5000):
        m = (1 << i) - 1
        t = m << (i - 1)
        # 当p为素数且梅森数2^p-1为素数时2^(p-1)*(2^p-1)为完全数
        if is_prime(i) and primality(i, m):
            count += 1
            num_len = len(str(t))
            str_content = (
                str_content
                + "第"
                + str(count)
                + "个"
                + str(num_len)
                + "位数："
                + str(t)
                + "\r\n"
            )
    end = datetime.datetime.now()
    print(str_content)
    print("find_perfect_number 运行花费时间为：", (end - begin).total_seconds(), "s")


find_perfect_number()
