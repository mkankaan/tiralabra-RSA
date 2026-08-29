from random import getrandbits
from math import floor, sqrt

from miller_rabin import miller_rabin


def generate_prime(bits, small_primes):
    """Generate a prime number.

    Args:
        bits (int): Bit length
        small_primes (list[int]): A list of the smallest prime numbers

    Returns:
        p (int): A prime number
    """

    p = getrandbits(bits)

    while not is_prime(p, small_primes):
        p = getrandbits(bits)

    return p


def is_prime(n, small_primes):
    """Determine if a number is prime.
    
    First check divisibility by small primes, if no small
    prime factors are found then run the Miller-Rabin test.

    Args:
        n (int): A prime candidate
        small_primes (list[int]): A list of the smallest prime numbers

    Returns:
        bool: False if n is composite, True if n is a probable prime
    """

    for p in small_primes:
        if n%p == 0:
            return False

    return miller_rabin(n)


def sieve_of_eratosthenes(n):
    """Generates a list of prime numbers by sieving out multiples.

    Args:
        n (int): The upper bound for the primes to list (inclusive)

    Returns:
        list[int]: A list of prime numbers
    """

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
