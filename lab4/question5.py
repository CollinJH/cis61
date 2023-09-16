def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a > b:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    if a < b or a == b:
        if a == 0:
            return b
        else:
            return gcd(a, b % a)


