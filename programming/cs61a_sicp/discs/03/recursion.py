# Recursive Multiplication
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m == 0 or n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)

# Fix bug in recursion
# Ans: The base case given is wrong, and it will get stuck in recursion when n = 3 for example
# Also the return in base case is off, as it should not always return 2 since it doesn't account
# for odd numberl like n = 5
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    # if n == 2: (wrong base case)
    #     return 2
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # write a helper function
    # check for divisibility
    def check_prime(x):
        if x >= 2:
            return n % x != 0 and check_prime(x-1)
        return True
    return check_prime(n-1)

# recursive hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
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
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    # if n is odd > n * 3 + 1 else n / 2
    # repeat until 1 (base case) > return 1
    print(n)
    if n == 1:
        return n
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone((n * 3) + 1)

def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    if n1 < 10 or n2 < 10:
        return int(str(max(n1, n2)) + str(min(n1, n2))) 
    return int(str(merge(max(n1,n2)//10, min(n1,n2)//10)) + str(merge(max(n1, n2)%10, min(n1,n2)%10)))