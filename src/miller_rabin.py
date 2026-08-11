from random import randrange


# n = odd prime candidate, n > 2
# k = level of accuracy (the number of witnesses tested against)
# Return: False (composite) or True (probably prime)
def miller_rabin(n, k=40):
    # n-1 = (2^s)*d
    (s, d) = factor_powers_of_two(n)

    # Generate a random witness and test if common divisors are found, repeat k times
    for _ in range(k):
        a = randrange(2, n-1) # Witness

        # For any given 1 < a < n-1, n is a strong probable prime if
        # one of these conditions holds:
        # 1) a^d = 1 (mod n)
        # 2) a^[(2^r)*d] = -1 (mod n)     for some 0 <= r < s

        x = pow(a, d, n)

        if x == 1 or x == n-1:
            # Condition 1 holds, continue to the next witness
            continue

        # Keep squaring x and taking mod n up to s times
        for _ in range(s):
            x = (x*x)%n

            if x == n-1:
                # Condition 2 holds, continue to the next witness
                continue

        if x != 1:
            return False # Composite

    # n wasn't proven to be composite, probable prime
    return True


# Factor out the largest power of 2 from n-1
# Return a tuple (s, d) such that n-1 = (2^s)*d, where s, d > 0 and d is odd
def factor_powers_of_two(n):
    s = 1
    result = n >> 1 # Right bit shift (division by 2)

    while result % 2 == 0:
        s += 1
        result = result >> 1

    return (s, result)
