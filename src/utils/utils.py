from math import floor, sqrt

# n = upper bound for the list of primes
def sieve_of_eratosthenes(n):
    if n < 2:
        return
    
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, floor(sqrt(n))+1):
        if primes[i]:
            for j in range(pow(i, 2), n+1, i):
                primes[j] = False
    return primes


# n = prime candidate, n > 2
# k = accuracy
# return: False (composite) or True (probably prime)
def miller_rabin(n, k):

    return

