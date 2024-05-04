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

# Q2
def infinite_generator(n):
    yield n
    while True:
        n += 1
        yield n

# next(infinite_generator) # Error: Type Error 'function' object is not iterable

gen_obj = infinite_generator(1)
next(gen_obj) # 1

next(gen_obj) # 2

# list(gen_obj) # Error: infinite loop

def rev_str(s):
    for i in range(len(s)):
        yield from s[i::-1]

hey = rev_str("hey")
next(hey) # y
next(hey) # e
next(hey) # h

list(hey) # -> ['y', 'e', 'h']

def add_prefix(s, pre):
    if not pre:
        return
    yield pre[0] + s
    yield from add_prefix(s, pre[1:])

school = add_prefix("schooler", ["pre", "middle", "high"])
next(school) # preschooler

list(map(lambda x: x[:-2], school)) # ["middleschool", "highschool"]

def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    yield from filter(lambda x: f(x), iterable)


def differences(it):
    """ 
    Yields the differences between successive terms of iterable it.

    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    it_lst = list(it) 
    if len(it_lst) < 2:
        return []
    else:
        yield from [it_lst[i+1] - it_lst[i] for i in range(len(it_lst)-1)]

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    prime_lst = []
    while n > 1:
        if is_prime(n):
            prime_lst.append(n)
        n -= 1
    yield from prime_lst