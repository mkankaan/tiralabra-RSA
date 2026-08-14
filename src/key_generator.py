from math import gcd, lcm

from sieve_of_eratosthenes import sieve_of_eratosthenes
from prime_generator import generate_prime
from key import Key


MAX_SMALL_PRIME = 3990
PUBLIC_EXPONENT = 65537 # Common public exponent


def generate_keys(key_length):
    """Generate a pair of RSA keys

    Args:
        key_length (int): The key length in bits

    Returns:
        (tuple): tuple containing:

            public_key (Key): An RSA public key
            private_key (Key): An RSA private key 
    """

    small_primes = sieve_of_eratosthenes(MAX_SMALL_PRIME)

    p = generate_prime(key_length, small_primes)
    q = generate_prime(key_length, small_primes)

    while p == q: # pragma: no cover
        q = generate_prime(key_length, small_primes)

    n = p*q
    least_common_multiple = lcm(p-1, q-1)

    public_key = Key(n, PUBLIC_EXPONENT)

    d = mod_inverse(PUBLIC_EXPONENT, least_common_multiple)
    private_key = Key(n, d)

    return (public_key, private_key)


def mod_inverse(n, m):
    """Find a modular multiplicative inverse of n (modulo m)

    Args:
        n (int): The value whose modular multiplicative inverse to find
        m (int): The modulus

    Returns:
        x (int): A value that satisfies n*x (mod m) = 1 or None if no solution exists
    """

    # No solution exists if n and m are not coprime
    if gcd(n, m) != 1:
        return None

    # Store the initial value of the modulus
    m_0 = m

    # Initial coefficients of x and y in the equation n*x + m*y = gcd(n, m) (Bézout's identity)
    (x, y) = (1, 0)

    # Steps of the extended Euclidean algorithm
    while n > 1:
        q = n//m
        (n, m) = (m, n%m)
        (x, y) = (y, x-q*y)

    if x < 0:
        x += m_0

    return x
