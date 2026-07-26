import random
from utils.utils import miller_rabin, small_primes_as_integers


def generate_two_primes():
    return


def generate_prime(bits):
    p = random.getrandbits(bits)
    print("got number with ", bits, " bits: ", p)
    # check primality

    p = 7309 # for testing
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


# n = prime candidate
def is_prime(n, s, d):
    MAX_SMALL_PRIME = 4000 # There are approx 500 primes < 4000
    small_primes = small_primes_as_integers(MAX_SMALL_PRIME) #The Sieve of Eratosthenes

    # Check if n is divisible by any small prime
    if is_divisible(n, small_primes):
        print(n, " is not prime")
        return False

    k = 40 # Miller-Rabin rounds
    print(miller_rabin(n, k, s, d))


# n = a prime candidate
# list = a list of numbers (small primes)
# Return True if n is divisible by any number in the list, otherwise False
def is_divisible(n, list):
    for p in list:
        if n%p == 0:
            print(n, " is divisible by ", p)
            return True
    print(n, " is not divisible by any small prime")
    return False
