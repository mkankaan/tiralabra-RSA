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

        self.very_large_primes = [73580281023602955967,
                                30944259551900547091,
                                70626262335815172977,
                                80097875640649218487,
                                24966924372157879961,
                                84576165284461385957,
                                1402831778467485618750058520099564728739064314447441300095347025131825574355721804363615723417369787,
                                7149045803847698137466342704076284829349022727161850664200751730703552909589658799810490226231340969,
                                6872692783987821972107370477617695856766942673732999168602273617108444392259273160078377252722386499]

    def test_is_prime_returns_correct_result_if_prime(self):
        for p in self.large_primes:
            self.assertTrue(is_prime(p))


    def test_is_prime_returns_correct_result_if_small_composite(self):
        for p in self.small_factor_composites:
            self.assertFalse(is_prime(p))


    def test_is_prime_returns_correct_result_if_large_composite(self):
        for p in self.large_factor_composites:
            self.assertFalse(is_prime(p))


    def test_very_large_primes(self):
        for p in self.very_large_primes:
            self.assertTrue(is_prime(p))
