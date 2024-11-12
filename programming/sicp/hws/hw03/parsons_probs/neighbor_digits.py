def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    count, curr_digit = 0, num % 10
    left_digit = num // 10 % 10
    if num == 0:
        return count
    if curr_digit == prev_digit or left_digit == curr_digit:
        count += 1
    return count + neighbor_digits(num // 10, curr_digit)