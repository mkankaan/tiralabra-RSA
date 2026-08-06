from random import getrandbits
from miller_rabin import miller_rabin


def generate_prime(bits, small_primes):
    p = getrandbits(bits)

    while not is_prime(p, small_primes):
        p = getrandbits(bits)

    return p


# n = prime candidate
# n = list of small primes
def is_prime(n, small_primes):
    # Check if n is divisible by any small prime
    for p in small_primes:
        if p%n == 0:
            return False

    return miller_rabin(n)
