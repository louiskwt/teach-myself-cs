# HOF

def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    """ print out all ints 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n):
        if cond(i):
            print(i)



def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ...     # Even numbers have remainder 0 when divided by 2.
        ...     return x % 2 == 0
        >>> make_keeper(5)(is_even)
        2
        4
    """
    def h(cond):
        for i in range(1, n):
            if cond(i):
                print(i)
    return h

