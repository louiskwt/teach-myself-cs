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
    def count_helper(n, k):
        count = 0
        while k > 0:
            if n == k or k == 1:
                count += 1
            else:
                count += count_helper(n, k-1)

        return count
    
    return count_helper(n, k)

# print(count_k(300, 1))


print("______________End of Q2________________")
#3.1 What would python display
a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])  # >>> 1, 3

len(a) # >>> 5
print(2 in a) # >>> False
print(4 in a) # >>> True
print(a[3][0]) # >>> 2

