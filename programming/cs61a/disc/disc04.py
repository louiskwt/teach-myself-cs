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

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False

    """
    if n == 1:
        return False

    def prime_helper(n, k):
        if n % k == 0:
            return False
        elif k + 1 == n:
            return True
        else:
            return prime_helper(n, k+1)
    return prime_helper(n, 2)

print(is_prime(7))
print(is_prime(3))
print(is_prime(4))
print(is_prime(10))
