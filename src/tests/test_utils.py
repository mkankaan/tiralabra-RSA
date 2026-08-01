import unittest
from utils.utils import mod_inverse

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_inputs = [(3, 11),
                            (10, 17),
                            (138533449, 69249218),
                            (2007956869, 501966760),
                            (1127126929, 93921300)]

        self.correct_results = [4, 12, 14188841, 183778989, 86113069]

        self.not_coprimes = [(6,20), (15589, 7361), (168760, 152874), (24240096, 10612959)]
        

    def test_mod_inverse_returns_correct_result(self):
        for i in range(len(self.test_inputs)):
            (n, m) = self.test_inputs[i]
            result = mod_inverse(n, m)
            self.assertEqual(result, self.correct_results[i])


    def test_mod_inverse_remainder_is_one(self):
        for i in range(len(self.test_inputs)):
            (n, m) = self.test_inputs[i]
            result = mod_inverse(n, m)
            self.assertEqual((n*result)%m, 1)


    def test_mod_inverse_returns_none_if_arguments_not_coprime(self):
        for (n, m) in self.not_coprimes:
            self.assertIsNone(mod_inverse(n, m))
        

    def test_mod_inverse_result_in_correct_range(self):
        for i in range(len(self.test_inputs)):
            (n, m) = self.test_inputs[i]
            result = mod_inverse(n, m)
            self.assertGreater(result, 0)
            self.assertLess(result, m)

