import time

# from timeit import timeit
# 1.96 seconds
# hxm-arch: 2 * 10**6 : 0.556 seconds
# hxm-arch: 2 * 10**8 : 63.036 seconds

start = time.time()

N = 2 * 10**8
SUM = 0
prime = []
for i in range(N + 1):
    prime.append(True)
for i in range(2, N + 1):
    if prime[i]:
        # print(i, end=' ')
        j = i + i
        while j <= N:
            prime[j] = False
            j += i


end = time.time()
print("Took %.3f seconds." % (end - start))
# print(f"Took {end - start}.3f seconds.")
