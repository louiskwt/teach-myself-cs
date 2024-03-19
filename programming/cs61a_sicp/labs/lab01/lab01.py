def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1 
    elif k == 1:
        return n
    else:
        factorial = n
        while k != 1:
            k -= 1
            factorial = factorial * (n - k)  
        return factorial



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count, integer = 0, 1
    while integer <= n:
        if integer % k == 0:
            print(integer)
            count += 1
        
        integer += 1
    
    return count

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    if y < 10:
        return y
    
    curr, sum = y, 0
    while curr >= 10:
        sum += curr % 10
        curr = curr // 10
    
    sum += curr
    
    return sum 


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n <= 10:
        return False
    
    curr, has_double_eights = n, False
    while curr > 10 and not has_double_eights:
        curr_digit = curr % 10
        next_digit = (curr // 10) % 10
        if curr_digit == 8 and next_digit == 8:
            has_double_eights = True
        
        curr = curr // 10
        
    return has_double_eights


