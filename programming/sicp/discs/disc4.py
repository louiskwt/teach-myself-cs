def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n <= 0:
        return 0
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    if n == 0 or k == 1:
        return 1
    total, i = 0, 1 
    while i < k:
        total += count_k(n - i, k)
        i += 1
    return count_k(n - k, k) + total


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    # s[0] * max_product(s[2:]) pick current one times everything that's non consecutive
    # s[1:] --> skip the current one and start on the next one
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))