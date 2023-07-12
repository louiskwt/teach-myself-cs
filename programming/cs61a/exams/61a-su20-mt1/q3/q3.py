email = 'example_key'

def maxkd(meteor, k):
    """
    Given a number `meteor`, finds the largest number of length `k` or fewer,
    composed of digits from `meteor`, in order.

    >>> maxkd(1234, 1)
    4
    >>> maxkd(32749, 2)
    79
    >>> maxkd(1917, 2)
    97
    >>> maxkd(32749, 18)
    32749
    """
    def concat(a, b):
        """
            a > b
        """
        return int(f"{a}{b}")

    total = len(str(meteor))

    if total < k:
        return meteor

    result = None

    while meteor // 10 >= 1:
        d = meteor % 10
        meteor = meteor // 10
        prev_defined = False
        prev = None
        if prev_defined:
            if d > prev and len(str(result)) < k:
                result = concat(d, result)
            prev = d
        else:
            prev = d
            result = d
            prev_defined = True

        print(f"result {result}, prev {prev}")
        if len(str(result)) == k:
            break


    return result

    #if ______:
     #   return ______
    #a = ______
   # b = ______
    #return ______

# ORIGINAL SKELETON FOLLOWS

# def maxkd(meteor, k):
#     """
#     Given a number `meteor`, finds the largest number of length `k` or fewer,
#     composed of digits from `meteor`, in order.

#     >>> maxkd(1234, 1)
#     4
#     >>> maxkd(32749, 2)
#     79
#     >>> maxkd(1917, 2)
#     97
#     >>> maxkd(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
