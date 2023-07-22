# Recursive Steps
# Figure out the base case 
# Make recursive call with a simpler statement until it reaches the base case
# Use the recursive call to solve the whole problem

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n-1)

assert multiply(6, 3) == 18
