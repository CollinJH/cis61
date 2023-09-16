from math import sqrt

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def is_prime_helper(n, k = 2):
        if n <= 2:
            return True
        elif n % k == 0:
            return False
        elif k < sqrt(n):
            return is_prime_helper(n, k + 1)
        return True
    return is_prime_helper(n)
     
