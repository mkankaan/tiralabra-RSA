import unittest
from sieve_of_eratosthenes import sieve_of_eratosthenes
from tests.primes import small_primes

class TestSieveOfEratosthenes(unittest.TestCase):
    def setUp(self):
        pass


    def test_sieve_returns_correct_list(self):
        n = max(small_primes)+1
        test_list = sieve_of_eratosthenes(n)
        self.assertEqual(test_list, small_primes)


    def test_sieve_returns_empty_list_if_input_less_than_two(self):
        self.assertEqual(sieve_of_eratosthenes(1), [])


    def test_sieve_returns_empty_list_if_input_zero(self):
        self.assertEqual(sieve_of_eratosthenes(0), [])


    def test_sieve_returns_empty_list_if_input_negative(self):
        self.assertEqual(sieve_of_eratosthenes(-3), [])


    def test_sieve_returns_first_prime(self):
        self.assertEqual(sieve_of_eratosthenes(2), [2])
    