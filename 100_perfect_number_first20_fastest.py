# Python实现，由于Python底层运算直接用C或C+++实现所以比Java运算快一些
import datetime
def isPrime(N):
    if N < 4: return N > 1
    if ((N & 1) == 0): return False
    i = 3
    while i * i <= N :
        if (N % i) == 0 : return False
        i += 2
    return True
def primality(N, M):
    if N == 2 : return True
    s = 4
    for i in range(0, N - 2) :
        s = (s * s - 2) % M
    return s == 0
def findPerfectNumber() :
    count = 0
    begin = datetime.datetime.now()
    strContent = ""
    for i in range(2, 5000):
        M = (1 << i) - 1
        t = M << (i-1)
        # 当p为素数且梅森数2^p-1为素数时2^(p-1)*(2^p-1)为完全数
        if isPrime(i) and primality(i,M) :
            count += 1
            numLen = len(str(t))
            strContent = strContent + "第" + str(count) + "个" + str(numLen) + "位数：" + str(t) + "\r\n"
    end = datetime.datetime.now()
    print(strContent)
    print("FindPerfectNumber运行花费时间为：", (end - begin).total_seconds(), "s")
findPerfectNumber()