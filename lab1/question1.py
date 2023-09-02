from operator import sub, mul, add


# Question 1 Part 2  
def twenty_twenty_three():
    """Come up with the most creative expression that evaluates 
    to 2023,using only numbers and the +, *, and - operators.
    (no call expressions)
    >>> twenty_twenty_three()
    2023
    """
    return sub(mul(add(mul(31,  42), 42), 42), 54425)
    #return ((((31 * 42) + 42) * 42) - 54425)



