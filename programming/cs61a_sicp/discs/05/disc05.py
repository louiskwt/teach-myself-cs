# Q1
from math import gcd

def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    cd = gcd(num, den)
    return [(num//cd), (den//cd)]

def numer(rat):
    """Extracts the numerator from a rational number."""
    return rat[0]

def denom(rat):
    """Extracts the denominator from a rational number."""
    return rat[1]

def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    return make_rat(numer(x)*denom(y), denom(x)*numer(y))


def lt_rat(x, y):
    """Returns True iff x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    return (numer(x)/denom(x)) < (numer(y)/denom(y))


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

# t = tree(1, [tree(2), tree(4)])

# label(t) # 1
# t[0] # 1
# label(branches(t)[0])  # 2
# is_leaf(t[1:][1]) # True
# [label(b) for b in branches(t)] # [2, 4]
# branches(tree(5, [t, tree(3)]))[0][0] # 1


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    def calculate_height(t, h=0):
        if is_leaf(t):
            return 1
        else:
            return h + max([calculate_height(b, 1) for b in branches(t)])
    return calculate_height(t)

def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if is_leaf(t) and label(t) != x:
        return None
    
    if label(t) == x:
        return [label(t)]
    
    path = None
    for b in branches(t):
        b_path = find_path(b, x)
        if find_path(b, x):
            path = [label(t)] + b_path
    return path


# Q1
# s = "cs61a"
# s_iter = iter(s)
# next(s_iter) --> c
# next(s_iter) --> s
# next(s_iter) --> 6

s = [[1, 2, 3, 4]]
i = iter(s)
j = iter(next(i))
# next(j) --> 1 
# s.append(5)
# next(i) --> 5
# next(j) --> 2
# list(j) --> [2,3,4]
# next(i) --> StopIteration