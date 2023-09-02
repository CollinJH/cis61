import math

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """

    "*** YOUR CODE HERE ***"
    total = 0
    while n != 0:
        total = total + (n % 10)
        n = math.floor(n / 10)
    return total

