from prime_generator import generate_two_primes
from classes.public_key import PublicKey
from classes.private_key import PrivateKey
from utils import mod_inverse, lcm
from math import ceil


class UI:
    def __init__(self):
        self.key_length = 512 # 1024


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
        (p, q) = generate_two_primes(self.key_length)
        n = p*q
        least_common_multiple = lcm(p-1, q-1)

        public_key = PublicKey(n)

        d = mod_inverse(public_key.exponent, least_common_multiple)
        private_key = PrivateKey(n, d)

        print()
        print("Public key:")
        print(public_key)
        print()
        print("Private key:")
        print(private_key)
        print()


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
        
        # Message encoded into an integer
        m = int.from_bytes(plaintext_message.encode("utf-8"))

        while m.bit_length() > self.key_length:
            plaintext_message = input("The message is too long, please give a shorter message: ")
            m = int.from_bytes(plaintext_message.encode("utf-8"))

        cipher_message = pow(m, e, n) # m^d % n

        print()
        print("Encrypted message:")
        print(cipher_message)
        print()


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

        int_message = pow(cipher_message, d, n) # c^d % n
        bytes = ceil(int_message.bit_length()/8)
        plaintext_message = int_message.to_bytes(bytes).decode("utf-8")

        print()
        print("Decrypted message:")
        print(plaintext_message)
        print()
