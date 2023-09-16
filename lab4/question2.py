def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    def hailstone_helper(n, count):
        if n == 1:
            print(int(n))
            return count + 1
        elif n % 2 == 0:
            print(int(n))
            return hailstone_helper((n / 2), count + 1)
        elif n % 2 != 0:
            print(int(n))
            return hailstone_helper((n * 3) + 1, count + 1)
    return hailstone_helper(n, 0)
