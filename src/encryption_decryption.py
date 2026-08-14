def encrypt(n, e, message):
    """Converts a plaintext message into ciphertext.

    Converts the message string into an integer, then performs
    modular exponentiation with regards to the RSA public key components
    passed as input.

    Args:
        n (int): The modulus of an RSA key
        e (int): The exponent of an RSA public key
        message (str): A plaintext message to encrypt

    Returns:
        int: The message converted into ciphertext
    """

    if message == "":
        return ""

    # Message encoded into an integer
    m = int.from_bytes(message.encode("utf-8"))

    if m.bit_length() > n.bit_length():
        return None

    cipher = pow(m, e, n) # m^e % n
    return cipher


def decrypt(n, d, cipher):
    """Converts a ciphertext message into plaintext.

    Performs modular exponentiation on the ciphertext with regards to the
    RSA private key components passed as input. Then converts the resulting
    integer into the original plaintext message.

    Args:
        n (int): The modulus of an RSA key
        d (int): The private exponent of an RSA key
        cipher (int): A ciphertext message to decrypt

    Returns:
        str: The ciphertext decrypted into plaintext
    """

    if cipher == "":
        return ""

    int_message = pow(cipher, d, n) # c^d % n
    message_bytes = (int_message.bit_length()+7)//8
    message = int_message.to_bytes(message_bytes).decode("utf-8")
    return message
