from sieve_of_eratosthenes import primes_up_to
from prime_generator import generate_prime
from math import gcd, lcm
from key import Key


MAX_SMALL_PRIME = 3990
KEY_LENGTH = 1024
PUBLIC_EXPONENT = 65537 # Common public exponent


def generate_keys():
    small_primes = primes_up_to(MAX_SMALL_PRIME) # Sieve of Eratosthenes
    
    p = generate_prime(KEY_LENGTH, small_primes)
    q = generate_prime(KEY_LENGTH, small_primes)
    
    while p == q:
        q = generate_prime(KEY_LENGTH, small_primes)

    n = p*q
    least_common_multiple = lcm(p-1, q-1)

    public_key = Key(n, PUBLIC_EXPONENT)

    d = mod_inverse(PUBLIC_EXPONENT, least_common_multiple)
    private_key = Key(n, d)

    return (public_key, private_key)


# Modular multiplicative inverse, a variant of the extended euclidean algorithm
# n*x + m*y = gcd(n, m) where gcd(n, m) = 1. Take (mod m) on both sides, giving n*x (mod m) = 1.
# Return x that satisfies the equation
def mod_inverse(n, m):
    # No solution exists if n and m are not coprime
    if gcd(n, m) != 1:
        return None

    #if m == 1:
    #    return 0

    m_0 = m # Initial value of the modulus
    (x, y) = (1, 0)

    while n > 1:
        q = n//m # Quotient
        (n, m) = (m, n%m)
        (x, y) = (y, x-q*y)

    if x < 0:
        x += m_0

    return x
