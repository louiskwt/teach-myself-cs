# truthy value (True, a non-zero integer, etc.)
# falsy value (False, 0, None, "", [], etc.).

def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case() # 12

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

just_in_case() # 19

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

case_in_point() # 12

'''
special_case and case_in_point result in the same output. 
For case_in_point, putting a return statement after the condition statement means it won't consider the rest of the body if the condition is true. 
For special case, when the one of the condition is evaluated to true, the rest of the elif block will not be evaluated
'''

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return True if temp < 60 or raining else False

def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    unit_digit = n % 10
    upper, lower = n + (10 - unit_digit), n - unit_digit 
    return lower if n % 10 < 5 else upper



# def square(x):
#     print("here!")
#     return x * x

# def so_slow(num):
#     x = num
#     while x > 0:
#         x = x + 1
#     return x / 0

# square(so_slow(5))

# ^ infinite loop, as x will keep increasing

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        msg = i
        if i % 3 == 0:
            msg = 'fizzbuzz' if i % 5 == 0 else 'fizz'
        if i % 5 == 0:
            msg = 'fizzbuzz' if i % 3 == 0 else 'buzz'
        print(msg)
        i += 1

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if n % i == 0 and (i > 1 and i < n):
            return False
        i += 1
    return n > 1

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while n >= 10:
        if not has_digit(n // 10, n % 10):
            count += 1
        n = n // 10
    return count

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n >= 10:
        if n % 10 == k:
            return True
        n = n // 10
    return n == k 

# notes  Assignments for def statements use pointers to functions, 