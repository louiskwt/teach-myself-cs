def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    if x > y:
        return []
    elif x == y:
        return [[x]]
    else:
        print(x)
        a = [x] + paths(x+1, y)[0]
        b = []
        if x*2 < y:
            b = [x] + paths(x*2, y)[1]
        elif x*2 == y:
            b = [x] + paths(x*2, y)[0]
        return [a, b]