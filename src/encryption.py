def encrypt(n, e, message):
    # Message encoded into an integer
    m = int.from_bytes(message.encode("utf-8"))

    # Message must have fewer bits than key
    if m.bit_length() > n.bit_length():
        return None
    return pow(m, e, n) # m^e % n
