def count_k(n, k,):
    """ 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1
    """
    #base case
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        count = 0
        i = 1
        while i <= k:
            count = count + count_k(n - i, k)
            i = i + 1
        return count
