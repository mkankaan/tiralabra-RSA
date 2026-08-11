from random import getrandbits
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
    
    First check divisibility by small primes, if no factors are found
    then check primality with the Miller-Rabin algorithm.

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
