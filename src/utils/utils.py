from math import floor, sqrt
from random import randrange

# n = upper bound for the list of small primes
def sieve_of_eratosthenes(n):
    if n < 2:
        return
    
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, floor(sqrt(n))+1):
        if primes[i]:
            for j in range(pow(i, 2), n+1, i):
                primes[j] = False


    ###### for testing
    primes_list = []
    for i in range(len(primes)):
        if primes[i]:
            primes_list.append(i)
    #print("small primes length: ", len(primes_list))
    ######

    return primes


# Helper function that takes a boolean list corresponding to primality of index as argument
# Returns a list of primes up to n as integers
def small_primes_as_integers(n):
    primes_boolean = sieve_of_eratosthenes(n)
    primes_int = [i for i in range(n) if primes_boolean[i]]
    return primes_int


# n = prime candidate, n > 2
# k = accuracy (the number of rounds)
# Return: False (composite) or True (probably prime)
def miller_rabin(n, k, s, d):
    witnesses = set()

    # Loop k times
    for i in range(k):
        a = randrange(2, n-1) # Witness

        while a in witnesses:
            a = randrange(2, n-1)
        witnesses.add(a)

        test_witness(a, s, d, n)
    
    #print("witnesses: ", witnesses)
    
    return True

def test_witness(a, s, d, n):
    x = pow(a, d)%n
    print("x: ", x)

    if abs(x) == 1:
        return True

    # loop s times
    
    return