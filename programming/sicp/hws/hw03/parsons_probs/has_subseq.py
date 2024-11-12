def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    # if seq == 0 == True
    # if n == 0 and seq != 0  False
    # n != seq % 10 --> n // 10 
    # n == seq % 10 --> seq // 10
    if n == 0 and seq != 0:
        return False
    if seq == 0:
        return True
    curr_digit, curr_element = n % 10, seq % 10 
    if curr_digit != curr_element:
        return has_subseq(n // 10, seq)
    if curr_digit == curr_element:
        return has_subseq(n // 10, seq // 10) 
