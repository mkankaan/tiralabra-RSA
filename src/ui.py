from utils import utils, prime_generator

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
                    print("generate keys")
                    BITS = 1024
                    prime = prime_generator.generate_prime(BITS)
                case "e":
                    print("encrypt")
                case "d":
                    print("decrypt")
                case _:
                    end = True
