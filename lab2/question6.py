def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

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
    print(n)
    counter = 1 
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            counter = counter + 1
            print(int(n))
        else:
            n = (n * 3) + 1
            counter = counter + 1
            print(int(n))
    return counter;
