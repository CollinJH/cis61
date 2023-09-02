from math import sqrt

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    k = 2
    if n <= 2:
        return False
    else:
        while k < sqrt(n):
            if n % k == 0:
                return False
            k = k + 1
    return True


