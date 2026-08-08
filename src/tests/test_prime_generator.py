import unittest
from prime_generator import generate_prime, is_prime
from tests.primes import small_primes, large_primes
from sympy import isprime


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        # Create composites with small factors (should be caught by the sieve)
        self.small_composites = [large_primes[i]*small_primes[i] for i in range(len(large_primes))]

        # Create composites with large factors (should go to Miller-Rabin):
        
        # Split the large primes into two lists
        large_factors_a = large_primes[:5]
        large_factors_b = large_primes[5:]
        # Multiply list items to create composites with large factors
        self.large_composites = [large_factors_a[i]*large_factors_b[i] for i in range(len(large_factors_a))]


    def test_is_prime_returns_correct_result_if_prime(self):
        for p in large_primes:
            self.assertTrue(is_prime(p, small_primes))


    def test_is_prime_returns_correct_result_if_small_composite(self):
        for p in self.small_composites:
            self.assertFalse(is_prime(p, small_primes))


    def test_is_prime_returns_correct_result_if_large_composite(self):
            for p in self.large_composites:
                self.assertFalse(is_prime(p, small_primes))


    # Test prime generation with SymPy's isprime() method
    # (Note that SymPy's primality checking is also probabilistic, not accurate)
    def test_generate_prime(self):
        bits = 1024

        for _ in range(10):
            test_prime = generate_prime(bits, small_primes)
            self.assertTrue(isprime(test_prime))
