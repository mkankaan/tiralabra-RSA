import unittest
from utils.miller_rabin import factor_powers_of_two

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_factor_powers_of_two_returns_correct_pair(self):
        numbers = [58303, 82459, 71037, 43337, 85451, 12557, 46609, 681547, 876263, 528897, 13, 41]

        correct_pairs = [(1, 29151),
                         (1, 41229),
                         (2, 17759), 
                         (3, 5417),
                         (1, 42725),
                         (2, 3139),
                         (4, 2913),
                         (1, 340773),
                         (1, 438131),
                         (9, 1033),
                         (2, 3),
                         (3, 5)]

        for i in range(len(numbers)):
            self.assertEqual(factor_powers_of_two(numbers[i]), correct_pairs[i])


    def test_factor_powers_of_two_d_always_odd(self):
        for i in range(301, 500, 2):
            d = factor_powers_of_two(i)[1]
            self.assertNotEqual(d%2, 0)
