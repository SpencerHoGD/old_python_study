from dectimeit import get_time

"""
print_count = 0.69 seconds
print_count = 0.49 seconds
2 Mollion home win = 0.307 seconds
20 Million home win = 3.381 seconds
200 Million home win = 36.218 seconds
200 Million home liam-arch = 10.251 seconds
200 Million home hxm-arch = 12.826 seconds

计算给定范围 n 内生成素数的个数
以及程序运行时间
"""


def prime_count(n):
    count = 0
    # prime = []
    # for i in range(n+1):
    #     prime.append(True)
    prime = [True] * (n + 1)
    for i in range(2, int(n**0.5 + 1.5)):
        if prime[i]:
            # print(i, end=' ')
            count += 1
            j = i * i
            while j <= n:
                prime[j] = False
                j += i
    print("\n", count)


@get_time
def prime_2(n):
    """
    给定 n 范围内，生成素数列表，打印列表长度（素数个数）
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5 + 1.5)):
        if not primes[i]:
            continue
        for j in range(i * i, n + 1, i):
            primes[j] = False
    primes = [i for i in range(n + 1) if primes[i]]
    # print(primes)
    print(len(primes))


if __name__ == "__main__":
    N = 2 * 10**8
    # prime_count(n)
    prime_2(N)
