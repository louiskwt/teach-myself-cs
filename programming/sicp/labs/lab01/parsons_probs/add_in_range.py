def add_in_range(start, stop):
    """
    >>> add_in_range(3, 5)  # .Case 1
    12
    >>> add_in_range(1, 10)  # .Case 2
    55
    """
    sum = start
    i, j = start, stop
    while i < j:
        i += 1
        sum += i
    return sum