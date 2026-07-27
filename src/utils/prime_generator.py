import random
from utils.utils import miller_rabin, small_primes_as_integers


def generate_two_primes():
    return


def generate_prime(bits):
    p = random.getrandbits(bits)
    print(p, "is prime?", is_prime(p))
    return p


# Return a tuple (s, d) such that n-1 = (2^s)*d
def factor_powers_of_two(n):
    s = 1

    while ((n-1)/pow(2,s)).is_integer():
        s += 1

    s -= 1
    d = int((n-1)/pow(2,s))
    return (s, d)


# n = prime candidate
def is_prime(p):
    MAX_SMALL_PRIME = 4000 # There are approx 500 primes < 4000
    small_primes = small_primes_as_integers(MAX_SMALL_PRIME) #The Sieve of Eratosthenes

    # Check if n is divisible by any small prime
    if is_divisible(p, small_primes):
        return False

    k = 40 # Miller-Rabin rounds
    return miller_rabin(p, k)


# n = a prime candidate
# list = a list of numbers (small primes)
# Return True if n is divisible by any number in the list, otherwise False
def is_divisible(p, numbers):
    for n in numbers:
        if p%n == 0:
            return True
    return False
