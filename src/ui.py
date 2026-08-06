from key_generator import generate_keys
from math import ceil
from encryption import encrypt


class UI:
    def __init__(self):
        pass

    def start(self):
        end = False
        while not end:
            user_input = input("[g]enerate keys, [e]ncrypt or [d]ecrypt. Press any other key to quit.\n")

            match user_input.lower():
                case "g":
                    (public_key, private_key) = generate_keys()
                    print(public_key)
                    print()
                    print(private_key)
                case "e":
                    (modulus, exponent, message) = self.get_encryption_inputs()
                    cipher = encrypt(modulus, exponent, message)

                    print()
                    print("Encrypted message:")
                    print(cipher)
                    print()
                case "d":
                    # ask cipher as input
                    #cipher = input()
                    #self.decrypt()
                    # tulosta viesti
                
                    print()
                    print("Decrypted message:")
                    print(message)
                    print()
                case _:
                    end = True


    def get_encryption_inputs(self):
        (n, e) = (None, None)
        
        while not n or not e:
            public_key = input("Recipient's public key: ")
            try:
                (n, e) = public_key.split("-")
                n = int(n)
                e = int(e)
            except ValueError:
                print("Please give a valid key")
                (n, e) = (None, None)

        message = input("Message to encrypt:\n")
        message_bits = int.from_bytes(message.encode("utf-8")).bit_length()

        while message_bits > n.bit_length():
            message = input("The message is too long, please give a shorter message:\n")
            message_bits = int.from_bytes(message.encode("utf-8")).bit_length()
        
        return (n, e, message)


    # siirrä
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
