import random

def generate_prime(bits):
    p = random.getrandbits(bits)
    print("got number with ", bits, " bits: ", p)
    return p

def generate_two_primes():
    return