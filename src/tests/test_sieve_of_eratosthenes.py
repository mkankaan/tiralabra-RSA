import unittest
from sieve_of_eratosthenes import sieve_of_eratosthenes
from tests.small_primes import small_primes

class TestSieveOfEratosthenes(unittest.TestCase):
    def setUp(self):
        pass


    def test_sieve_returns_correct_list(self):
        n = max(small_primes)+1
        test_list = sieve_of_eratosthenes(n)
        self.assertEqual(test_list, small_primes)
