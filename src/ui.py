from utils import prime_generator
from utils.utils import lcm, mod_inverse
from key import Key


class UI:
    def __init__(self):
        pass

    def start(self):
        end = False
        while not end:
            user_input = input("[g]enerate keys, [e]ncrypt or [d]ecrypt. Press any other key to quit.\n")

            match user_input.lower():
                case "g":
                    #BITS = 1024
                    BITS = 16 # for testing
                    (p, q) = prime_generator.generate_two_primes(BITS)

                    # for testing
                    p = 39511
                    q = 5701

                    n = p*q
                    least_common_multiple = lcm(p-1, q-1)

                    e = 65537 # Common public exponent
                    d = mod_inverse(e, least_common_multiple)

                    public_key = Key(n, e)
                    private_key = Key(n, d)

                    print("pub key:", public_key)
                    print("priv key:", private_key)
                case "e":
                    print("encrypt")
                case "d":
                    print("decrypt")
                case _:
                    end = True
