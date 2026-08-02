from math import floor, sqrt


# n = upper bound for the list of small primes
# Returns a boolean list corresponding to the primality of each index
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


# Helper function that returns a list of primes up to n as integers
def small_primes_as_integers(n):
    primes_boolean = sieve_of_eratosthenes(n)
    primes_int = [i for i in range(n) if primes_boolean[i]]
    return primes_int


# n = a prime candidate
# list = a list of numbers (small primes)
# Return True if n is divisible by any number in the list, otherwise False
def is_divisible(p, numbers):
    for n in numbers:
        if p%n == 0:
            return True
    return False
