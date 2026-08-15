import unittest
from key_generator import generate_keys, mod_inverse


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.coprimes = [(3, 11),
                        (10, 17),
                        (138533449, 69249218),
                        (2007956869, 501966760),
                        (1127126929, 93921300)]

        self.coprimes_correct_results = [4, 12, 14188841, 183778989, 86113069]
        self.not_coprimes = [(6,20), (15589, 7361), (168760, 152874), (24240096, 10612959)]


    def test_generated_keys_are_correct_length(self):
        bits = 1024

        for _ in range(10):
            modulus = generate_keys(bits)[0].modulus
            self.assertAlmostEqual(modulus.bit_length(), 2*bits, delta=100)


    def test_generates_valid_keys(self):
        (public_key, private_key) = generate_keys(1024)
        self.assertTrue(public_key.exponent == 65537)
        self.assertEqual(public_key.modulus, private_key.modulus)
        self.assertNotEqual(public_key.exponent, private_key.exponent)
    

    def test_mod_inverse_returns_correct_result(self):
        for i in range(len(self.coprimes)):
            (n, m) = self.coprimes[i]
            result = mod_inverse(n, m)
            self.assertEqual(result, self.coprimes_correct_results[i])


    def test_mod_inverse_returns_none_if_arguments_not_coprime(self):
        for (n, m) in self.not_coprimes:
            self.assertIsNone(mod_inverse(n, m))
