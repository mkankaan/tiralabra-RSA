import random
from miller_rabin import miller_rabin
from sieve_of_eratosthenes import small_primes_as_integers, is_divisible


def generate_two_primes(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)

    while p == q:
        q = generate_prime(bits)

    return (p, q)


def generate_prime(bits):
    p = random.getrandbits(bits)

    while not is_prime(p):
        p = random.getrandbits(bits)

    return p


# n = prime candidate
def is_prime(n):
    MAX_SMALL_PRIME = 4000 # There are approx 500 primes < 4000
    small_primes = small_primes_as_integers(MAX_SMALL_PRIME) #The Sieve of Eratosthenes

    # Check if n is divisible by any small prime
    if is_divisible(n, small_primes):
        return False

    k = 40 # Miller-Rabin rounds
    return miller_rabin(n, k)
