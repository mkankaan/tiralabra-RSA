import unittest
from miller_rabin import factor_powers_of_two


class TestMillerRabin(unittest.TestCase):
    def setUp(self):
        self.numbers = [58303, 82459, 71037, 43337, 85451, 12557, 46609, 681547, 876263, 528897, 13, 41,
                           73580281023602955967]
        
        self.correct_pairs = [(1, 29151),
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
                            (3, 5),
                            (1, 36790140511801477983)]


        # todo: add test cases for large values


    def test_factor_powers_of_two_returns_correct_pair(self):
        for i in range(len(self.numbers)):
            (s, d) = self.correct_pairs[i]
            self.assertEqual(factor_powers_of_two(self.numbers[i]), (s, d))
            self.assertEqual(self.numbers[i]-1, pow(2, s)*d)


    def test_factor_powers_of_two_results_match(self):
            for i in range(len(self.numbers)):
                (s, d) = self.correct_pairs[i]
                self.assertEqual(self.numbers[i]-1, pow(2, s)*d)


    def test_factor_powers_of_two_d_always_odd(self):
        for i in range(3, 500, 2):
            d = factor_powers_of_two(i)[1]
            self.assertNotEqual(d%2, 0)
