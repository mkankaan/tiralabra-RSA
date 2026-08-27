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

                    print("\nPublic key:\n")
                    print(public_key)
                    print()
                    print("Private key:\n")
                    print(private_key)
                    print()
                case "e":
                    print("Recipient's public key:")
                    (modulus, exponent) = self.get_user_key()
                    print()
                    message = None

                    while not message:
                        message = input("Message to encrypt:\n")
                        # Message encoded into an integer
                        message_int = int.from_bytes(message.encode("utf-8"))

                        if message == "":
                            print("Please enter a valid message")
                            message = None
                        elif  message_int.bit_length() > modulus.bit_length():
                            print("The message is too long, please give a shorter message")
                            message = None

                    cipher = encrypt(modulus, exponent, message)

                    print()
                    print("Encrypted message:\n")
                    print(cipher)
                    print()
                case "d":
                    print("Recipient's private key:")
                    (modulus, exponent) = self.get_user_key()
                    print()
                    cipher = None

                    while not cipher:
                        cipher = input("Message to decrypt:\n")
                        try:
                            cipher = int(cipher)
                        except ValueError:
                            print("Please give the message as ciphertext")
                            cipher = None

                    message = decrypt(modulus, exponent, cipher)

                    if not message:
                        print()
                        print("Unable to decrypt the message. Make sure to enter a valid private key and ciphertext.")
                        print()
                        continue

                    print()
                    print("Decrypted message:\n")
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
