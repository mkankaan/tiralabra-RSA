import unittest
from utils.utils import sieve_of_eratosthenes

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                        151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    def test_sieve_returns_list_of_correct_length(self):
        n = 199
        test_list = sieve_of_eratosthenes(n)
        self.assertEqual(len(test_list), n+1)

    def test_sieve_returns_all_primes(self):
        n = 199
        test_list = sieve_of_eratosthenes(n)

        for p in self.small_primes:
            self.assertEqual(test_list[p], True)

    def test_sieve_returns_only_primes(self):
        n = 199
        test_list = sieve_of_eratosthenes(n)
        self.assertEqual(sum(test_list), len(self.small_primes))

    def test_sieve_finds_large_primes(self):
        large_prime = 3989 # The smallest prime below 4000
        test_list = sieve_of_eratosthenes(4000)
        self.assertEqual(test_list[large_prime], True)
        self.assertEqual(sum(test_list[large_prime+1:]), 0)
