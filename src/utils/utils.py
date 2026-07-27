from math import floor, sqrt
from random import randrange
from prime_generator import factor_powers_of_two


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
    print("# of small primes:", len(primes_int))
    return primes_int


# n = prime candidate, n > 2
# k = level of accuracy (the number of rounds)
# Return: False (composite) or True (probably prime)
def miller_rabin(n, k):
    (s, d) = factor_powers_of_two(n)

    # Loop k times
    for i in range(k):
        a = randrange(2, n-1) # Witness

        if not test_witness(a, s, d, n):
            return False

    return True


def test_witness(a, s, d, n):
    x = pow(a, d, n) # (a^d) % n

    for i in range(s):
        y = pow(x, 2, n) # x^2 % n

        if nontrivial_square_root(y, x, n):
            return False
        x = y

    # n wasn't proven to be composite, so it's likely prime
    return True


def nontrivial_square_root(y, x, n):
    return y == 1 and x != 1 and x != n-1
