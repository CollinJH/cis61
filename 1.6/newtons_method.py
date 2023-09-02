# newtons method is an iterative improvement algorithm, it improves
# a guess of the zero for any function that is differentiable
# which means it can be approximated by a straight line at any point


# computational process of following the tangent line to 0
# for a function f and its derivative df

def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess;

def approx_eq(x, y, tolerance=1e-13):
    return abs(x - y) < tolerance

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

# for newtons method for a degree n root of a which is x such that 
# x * x * x = a as x is repeated n times

# nsqrt(a) = x or x^n - a = 0
# if we can find the 0 of the last equation we can compute the n roots

# firstly implementing square_root
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

# generalizing to roots of arbitary degree n now
# f(x) = x^n -a
# df(x) = n * x^n - 1

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)


