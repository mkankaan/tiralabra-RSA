def encrypt(n, e, m):
    return pow(m, e, n) # m^e % n


def decrypt(n, d, c):
    int_message = pow(c, d, n) # c^d % n
    message_bytes = (int_message.bit_length()+7)//8
    message = int_message.to_bytes(message_bytes).decode("utf-8")
    return message
