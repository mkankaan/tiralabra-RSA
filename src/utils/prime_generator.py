import random

def generate_prime(bits):
    p = random.getrandbits(bits)
    print("got number with ", bits, " bits: ", p)
    # check primality

    (s, d) = factor_powers_of_two(p)
    print(s, d)
    return p

def factor_powers_of_two(n):
    s = 1

    while ((n-1)/pow(2,s)).is_integer():
        s += 1

    s -= 1
    d = int((n-1)/pow(2,s))

    return (s, d)



def generate_two_primes():
    return