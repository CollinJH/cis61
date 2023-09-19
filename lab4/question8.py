def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def ten_pairs_counter(n, i, j, counter):
        str_n = str(n)
        length_n = len(str_n)
        
        # base case, last digit has been reached
        if i == length_n - 1:
            return counter


        digit_to_add_n = (n // (10 ** i)) % 10
        if digit_to_add_n + int(str_n[j]) == 10:
            counter += 1
        
        if j == length_n - 1:
            return ten_pairs_counter(n, i + 1, i + 2, counter)

        return ten_pairs_counter(n, i, j + 1, counter)
            
            





    return ten_pairs_counter(n, i = 0, j = 1, counter = 0)
            
