from random import randrange


def miller_rabin(n, k=40):
    """A test to determine if a number is a probable prime.
    Generate a given amount of random integers (witnesses) and test if
    common factors are found.

    For any given witness 1 < a < n-1, n is a strong probable prime
    if one of these conditions holds:

    1) a^d = 1 (mod n)
    2) a^[(2^r)*d] = -1 (mod n)     for some 0 <= r < s

    Args:
        n (int): A prime candidate
        k (int, optional): The amount of witnesses to test. Defaults to 40.

    Returns:
        bool: False if n is composite, True if n is a probable prime
    """

    (s, d) = factor_powers_of_two(n)

    for _ in range(k):
        a = randrange(2, n-1) # Witness
        x = pow(a, d, n)

        if x == 1 or x == n-1:
            # Condition 1 holds, continue to the next witness
            continue

        # Keep squaring x (mod n) up to s times
        for _ in range(s):
            x = (x*x)%n

            if x == n-1:
                # Condition 2 holds, continue to the next witness
                continue

        if x != 1:
            return False # Composite

    # n wasn't proven to be composite, probable prime
    return True


def factor_powers_of_two(n):
    """Factor out the largest power of 2 from an integer

    Args:
        n (int): An odd integer to deconstruct s.t. n-1 = (2^s)*d

    Returns:
        (tuple): tuple containing:
        
            s (int): The powers of 2 in n
            d (int): The multiplier of 2^s to make n-1
    """

    s = 1
    result = n >> 1 # Right bit shift (division by 2)

    while result % 2 == 0:
        s += 1
        result = result >> 1

    return (s, result)
