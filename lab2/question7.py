def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers

    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13

    """
    k = 0

    curr_fib, prev_fib, prev_prev_fib, = 0, 0, 0

    while k < n:
        if k == 0:
            k = k + 1
            curr_fib = k
        elif k == 1:
            prev_fib = curr_fib
            k = k + 1
        else:
            prev_prev_fib = prev_fib
            prev_fib = curr_fib
            curr_fib = prev_fib + prev_prev_fib
            k = k + 1
    return curr_fib
