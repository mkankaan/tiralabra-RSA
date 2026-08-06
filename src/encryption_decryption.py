def encrypt(n, e, message):
    # Message encoded into an integer
    m = int.from_bytes(message.encode("utf-8"))

    # Message must have fewer bits than key
    if m.bit_length() > n.bit_length():
        return None
    cipher = pow(m, e, n) # m^e % n
    return cipher


def decrypt(n, d, cipher):
    int_message = pow(cipher, d, n) # c^d % n
    bytes = (int_message.bit_length()+7)//8
    message = int_message.to_bytes(bytes).decode("utf-8")
    return message