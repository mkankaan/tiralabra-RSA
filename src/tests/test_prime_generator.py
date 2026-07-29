import unittest
from utils.prime_generator import is_prime

class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.large_primes = [723640097,
                            258366533,
                            659444129,
                            385965397,
                            230653477,
                            535052003,
                            689717351,
                            567635851,
                            267746111,
                            484999693]
                            
        # Composites with small factors (should be caught by the sieve)
        self.small_factor_composites = [self.large_primes[i]*(i+2) for i in range(len(self.large_primes))]

        # Composites with large factors (should go to Miller-Rabin)
        self.small_primes = [5039, 5051, 5059, 5077, 5081, 5087, 7069, 7079, 7103, 11243, 11251, 11257]
        self.large_factor_composites = [self.large_primes[i]*self.small_primes[i] for i in range(len(self.large_primes))]


    def test_is_prime_returns_correct_result_if_prime(self):
        for p in self.large_primes:
            self.assertTrue(is_prime(p))


    def test_is_prime_returns_correct_result_if_small_composite(self):
        for p in self.small_factor_composites:
            self.assertFalse(is_prime(p))


    def test_is_prime_returns_correct_result_if_large_composite(self):
        for p in self.large_factor_composites:
            self.assertFalse(is_prime(p))
