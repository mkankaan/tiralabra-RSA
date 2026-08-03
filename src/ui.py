from prime_generator import generate_two_primes
from classes.public_key import PublicKey
from classes.private_key import PrivateKey
from utils import lcm, mod_inverse
from math import ceil


class UI:
    def __init__(self):
        pass

    def start(self):
        end = False
        while not end:
            user_input = input("[g]enerate keys, [e]ncrypt or [d]ecrypt. Press any other key to quit.\n")

            match user_input.lower():
                case "g":
                    self.generate_keys()
                case "e":
                    self.encrypt()
                case "d":
                    self.decrypt()
                case _:
                    end = True


    def generate_keys(self):
        #BITS = 1024
        BITS = 16 # for testing
        (p, q) = generate_two_primes(BITS)

        # for testing
        #p = 39511
        #q = 5701

        n = p*q
        least_common_multiple = lcm(p-1, q-1)

        #e = 65537 # Common public exponent
        #d = mod_inverse(e, least_common_multiple)

        public_key = PublicKey(n)

        d = mod_inverse(public_key.exponent, least_common_multiple)
        private_key = PrivateKey(n, d)

        print("Public key:")
        print(public_key)
        print()
        print("Private key:")
        print(private_key)


    def encrypt(self):
        (n, e) = (None, None)
        
        # will be cleaned up and repetition will be removed
        while not n or not e:
            public_key = input("Recipient's public key: ")
            try:
                (n, e) = public_key.split("-")
                n = int(n)
                e = int(e)
            except ValueError:
                print("Please give a valid key")
                (n, e) = (None, None)

        plaintext_message = input("Message to encrypt: ")
        int_message = int.from_bytes(plaintext_message.encode("utf-8"))
        #print("int msg:", int_message)

        print("bits:", int_message.bit_length())

        cipher_message = pow(int_message, e, n) # message^d % n

        print("Encrypted message:")
        print(cipher_message)


    def decrypt(self):
        (n, d) = (None, None)
                            
        while not n or not d:
            public_key = input("Recipient's private key: ")
            try:
                (n, d) = public_key.split("-")
                n = int(n)
                d = int(d)
            except ValueError:
                print("Please give a valid key")
                (n, d) = (None, None)

        cipher_message = None

        while not cipher_message:
            cipher_message = input("Message to decrypt: ")
            try:
                cipher_message = int(cipher_message)
            except ValueError:
                print("Please give the message as ciphertext")
                cipher_message = None

        int_message = pow(cipher_message, d, n) # cipher^d % n
        print("int message:", int_message)

        bytes = ceil(int_message.bit_length()/8)
        plaintext_message = int_message.to_bytes(bytes, byteorder='big').decode("utf-8")
        print("Decrypted message:")
        print(plaintext_message)
