# Greatest common divisor
def gcd(a, b):
    if b > a:
        a, b = b, a
    
    if b == 0:
        return a

    return gcd(b, a%b)


# Least common multiple
def lcm(a, b):
    return int(abs(a*b)//gcd(a, b))


# Modular multiplicative inverse, a variant of the extended euclidean algorithm
# n*x + m*y = gcd(n, m) where gcd(n, m) = 1. Take (mod m) on both sides, giving n*x (mod m) = 1.
# Return x that satisfies the equation
def mod_inverse(n, m):
    # No solution exists if n and m are not coprime
    if gcd(n, m) != 1:
        return None

    #if m == 1:
    #    return 0

    m_0 = m # Initial value of the modulus
    (x, y) = (1, 0)

    while n > 1:
        q = n//m # Quotient
        (n, m) = (m, n%m)
        (x, y) = (y, x-q*y)

    if x < 0:
        x += m_0

    return x
