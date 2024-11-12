def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    n1_digit, n2_digit = n1 % 10, n2 % 10
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1_digit < n2_digit:
        return int(str(merge(n1 // 10, n2)) + str(n1_digit))
    else:
        return int(str(merge(n1, n2 // 10)) + str(n2_digit))

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
    print(n)
    if n == 1:
        return n
    next_num = n
    if n % 2 == 0:
        next_num = n // 2
    else:
        next_num = (n * 3) + 1
    return 1 + hailstone(next_num)

# check prime recursively
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime_helper(n, divisor):
        if n == 2:
            return True
        if n % divisor == 0:
            return False
        if divisor + 1 == n:
            return True
        return prime_helper(n, divisor + 1)
    return prime_helper(n, 2)