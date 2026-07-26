import random
from utils.utils import miller_rabin, sieve_of_eratosthenes


def generate_two_primes():
    return


def generate_prime(bits):
    p = random.getrandbits(bits)
    print("got number with ", bits, " bits: ", p)
    # check primality

    p = 53 # for testing
    (s, d) = factor_powers_of_two(p)
    print("s, d: ", s, d)

    is_prime(p, s, d)
    return p


# Return a tuple (s, d) such that n-1 = (2^s)*d
def factor_powers_of_two(n):
    s = 1

    while ((n-1)/pow(2,s)).is_integer():
        s += 1

    s -= 1
    d = int((n-1)/pow(2,s))

    print(n-1, " = ", "2^", s, "*", d)
    return (s, d)


def is_prime(n, s, d):
    MAX_SMALL_PRIME = 4000 # There are approx 500 primes < 4000
    small_primes = sieve_of_eratosthenes(MAX_SMALL_PRIME)
    # test if divisible with sieve
    k = 40 # Miller-Rabin rounds
    print(miller_rabin(n, k, s, d))