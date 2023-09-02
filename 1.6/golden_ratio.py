
# iterative improvement algorithm
# begins with a guess of a solution to an equation
# repeatedly applies an update function 
# applies a close comparison to check if the guess is close enough
def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess;

# tests approximation to tolerance
def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

# update function for golden ratio
def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)





