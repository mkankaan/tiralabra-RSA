from utils import prime_generator
from utils.utils import gcd, lcm, mod_inverse
from key import Key


class UI:
    def __init__(self):
        # Upper bound for the smallest prime we want to check with the sieve
        self.MAX_SMALL_PRIME = 4000

    def start(self):
        end = False
        while not end:
            user_input = input("[g]enerate keys, [e]ncrypt or [d]ecrypt. Press any other key to quit.\n")

            match user_input.lower():
                case "g":
                    #BITS = 1024
                    BITS = 16
                    (p, q) = prime_generator.generate_two_primes(BITS)

                    #print("p:", p)
                    #print("q:", q)

                    # for testing
                    p = 39511
                    q = 5701

                    n = p*q

                    #print("n:", n)

                    g = gcd(p-1, q-1)
                    print("gcd:", g)

                    l = lcm(p-1, q-1)
                    print("lcm:", l)

                    e = 65537 # Common public exponent

                    pubic_key = Key(n, e)
                    print("public key modulus:", pubic_key.modulus, " exp:", pubic_key.exponent)

                    d = mod_inverse(n, l) # mod_inverse(e, lcm)
                    print("d:", d)
                case "e":
                    print("encrypt")
                case "d":
                    print("decrypt")
                case _:
                    end = True
