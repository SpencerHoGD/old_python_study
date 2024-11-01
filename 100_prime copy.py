import math
import time
from timeit import timeit
"""
1.96 seconds
"""

start = time.time()

n = 2000000
sum = 0
prime = []
for i in range(n+1):
    prime.append(True)
for i in range(2, n+1):
    if prime[i]:
        # print(i, end=' ')
        j = i + i
        while j <= n:
            prime[j] = False
            j += i


end = time.time()
print('Took %.3f seconds.' % (end - start))
