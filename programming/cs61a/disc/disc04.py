# Recursive Steps
# Figure out the base case 
# Make recursive call with a simpler statement until it reaches the base case
# Use the recursive call to solve the whole problem

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    return m + multiply(m, n-1)

assert multiply(6, 3) == 18

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False

    """
    if n == 1:
        return False

    def prime_helper(n, k):
        if n % k == 0:
            return False
        elif k + 1 == n:
            return True
        else:
            return prime_helper(n, k+1)
    return prime_helper(n, 2)

# print(is_prime(7))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(10))

# n stairs problem with tree recursion
def count_stair_ways(n):
    """
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

print(count_stair_ways(4))
print(count_stair_ways(3))


print("____________End of Q3.1_______________")
# Q2.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    # no overstep, see how many way to reach n(0) / stop at 0
    #       n = 4, k = 2
    #               4
    #            2       3
    #         0 1         2   1
    #    -2 -1  0 -1   0 1     0 -1
    #                    -1 0
    # count the 0 => ways to reach n usuing up to k
    if n < 0:
        return 0 # stop
    if n == 0:
        return 1
    count = 0
    step = 1
    while step <= k:    # up to k (inclusive <=)
        count += count_k(n-step, k)
        step += 1
    return count

print(count_k(4, 2)) # => 5
print(count_k(300, 1))
print(count_k(3, 3))
print(count_k(4, 4))



print("______________End of Q2________________")
#3.1 What would python display
a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])  # >>> 1, 3

len(a) # >>> 5
print(2 in a) # >>> False
print(4 in a) # >>> True
print(a[3][0]) # >>> 2

print("_______________End of Q3.1_______________")

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [value * index for index, value in enumerate(s) if index % 2 == 0]

x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))

print("_______________End of Q3.2_______________")

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    total = len(s)
    if total == 0:
        return 1

    product_list = [0]*total # create a list of product that has the length of the s

    for i in range(total):
        if i == 0:
            product_list[i] = s[i]
        elif i == 1:
            product_list[i] = max(product_list[i-1], s[i]) # compare the two and take the larger one
        else:
            product_list[i] = max(product_list[i-2] * s[i], product_list[i-1]) 
            # compare non-consecutive product against the one before and take the larger one
    return product_list[-1]

print(max_product([10,3,1,9,2]))
print(max_product([5,10,5,10,5]))
print(max_product([]))

print("_______________End of Q3.3_______________")
# Whole number
def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    n_lst = [int(x) for x in str(n)]
    is_hole = True
    for i, num in enumerate(n_lst):
        if i < len(n_lst) - 2 and (i+1) % 2 != 0 and n_lst[i+1] > num:
            is_hole = False
    return is_hole

print(check_hole_number(123))
print(check_hole_number(968))
