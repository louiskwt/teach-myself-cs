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