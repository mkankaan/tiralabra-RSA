def encrypt(n, e, message):
    if message == "":
        return None

    # Message encoded into an integer
    m = int.from_bytes(message.encode("utf-8"))

    # Message must have fewer bits than key
    if m.bit_length() > n.bit_length():
        return None
    cipher = pow(m, e, n) # m^e % n
    return cipher


def decrypt(n, d, cipher):
    if cipher == "":
        return None

    int_message = pow(cipher, d, n) # c^d % n
    message_bytes = (int_message.bit_length()+7)//8
    message = int_message.to_bytes(message_bytes).decode("utf-8")
    return message
