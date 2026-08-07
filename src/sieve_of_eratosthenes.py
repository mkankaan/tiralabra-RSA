from math import floor, sqrt


# Returns a list of primes up to n
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, floor(sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    primes_list = [i for i in range(n+1) if primes[i]]
    return primes_list
