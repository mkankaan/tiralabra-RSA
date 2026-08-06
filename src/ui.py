from key_generator import generate_keys
from encryption_decryption import encrypt, decrypt


class UI:
    def __init__(self):
        pass


    def start(self):
        end = False
        while not end:
            user_input = input("[g]enerate keys, [e]ncrypt or [d]ecrypt. Press any other key to quit.\n")

            match user_input.lower():
                case "g":
                    print("Generating keys, please wait...")
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
                    (modulus, exponent, message) = self.get_decryption_inputs()
                    message = decrypt(modulus, exponent, message)

                    print()
                    print("Decrypted message:")
                    print(message)
                    print()
                case _:
                    end = True


    def get_encryption_inputs(self):
        (n, e) = (None, None)
        
        while not n or not e:
            key = input("Recipient's public key:\n")
            try:
                (n, e) = key.split("-")
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


    def get_decryption_inputs(self):
        (n, d) = (None, None)
                            
        while not n or not d:
            key = input("Recipient's private key:\n")
            try:
                (n, d) = key.split("-")
                n = int(n)
                d = int(d)
            except ValueError:
                print("Please give a valid key")
                (n, d) = (None, None)

        cipher = None

        while not cipher:
            cipher = input("Message to decrypt:\n")
            try:
                cipher = int(cipher)
            except ValueError:
                print("Please give the message as ciphertext")
                cipher = None

        return (n, d, cipher)
