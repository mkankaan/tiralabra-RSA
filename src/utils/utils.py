from math import floor, sqrt

def sieve_of_eratosthenes(n):
    if n < 2:
        return
    primes = [True]*(n+1)

    primes[0] = False
    primes[1] = False

    for i in range(2, floor(sqrt(n))):  
        if primes[i]:
            j = 0
            multiple = pow(i, 2)+(i*j)

            while multiple <= n:
                primes[multiple] = False
                j += 1
                multiple = pow(i, 2)+(i*j)

    print(primes)

    return primes
