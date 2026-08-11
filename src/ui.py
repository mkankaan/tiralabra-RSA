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
                    (public_key, private_key) = generate_keys(1024)
                    print(public_key)
                    print()
                    print(private_key)
                case "e":
                    print("Recipient's public key:")
                    (modulus, exponent) = self.get_user_key()
                    message = None

                    while not message:
                        message = input("Message to encrypt:\n")
                        message_bits = int.from_bytes(message.encode("utf-8")).bit_length()

                        if message == "":
                            print("Please enter a valid message")
                            message = None
                        elif  message_bits > modulus.bit_length():
                            print("The message is too long, please give a shorter message")
                            message = None

                    cipher = encrypt(modulus, exponent, message)

                    print()
                    print("Encrypted message:")
                    print(cipher)
                    print()
                case "d":
                    print("Recipient's private key:")
                    (modulus, exponent) = self.get_user_key()
                    cipher = None

                    while not cipher:
                        cipher = input("Message to decrypt:\n")
                        try:
                            cipher = int(cipher)
                        except ValueError:
                            print("Please give the message as ciphertext")
                            cipher = None

                    message = decrypt(modulus, exponent, cipher)

                    print()
                    print("Decrypted message:")
                    print(message)
                    print()
                case _:
                    end = True


    def get_user_key(self):
        (mod, exp) = (None, None)

        while not mod or not exp:
            key = input()
            try:
                (mod, exp) = key.split("-")
                mod = int(mod)
                exp = int(exp)
            except ValueError:
                print("Please give a valid key:")
                (mod, exp) = (None, None)

        return (mod, exp)
