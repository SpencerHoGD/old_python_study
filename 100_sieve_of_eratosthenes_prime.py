from dectimeit import get_time

@get_time
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    result = []
    for i in range(2, n+1):
        if primes[i]:
            result.append(i)

    return result

@get_time
def linear_sieve(n):
    is_prime = [True] * (n+1)
    primes = []

    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
        for j in primes:
            if i * j > n:
                break
            is_prime[i * j] = False
            if i % j == 0:
                break

    return primes
    print(len(primes))


if __name__ == '__main__':
    n = 2*10**8
    sieve_of_eratosthenes(n)
    # linear_sieve(n)  # slower 1 times