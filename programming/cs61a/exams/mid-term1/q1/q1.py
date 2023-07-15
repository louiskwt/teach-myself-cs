email = 'example_key'



def kv(prev=lambda x: 0):
    """
    A kv store is a store that associates keys with values.

    To create a kv store, call the function `kv`, to get a `put` function.
    This function enables you to "put" a key-value pair into the store, and
    returns two functions `get` and another `put`. The `get` function should
    let you look up a key and return its corresponding value, while the
    new `put` function should let you continue adding on to the existing
    kv store.

    Note that you can assume that every key provided is unique. If you try to
    get the value for a key that does not exist, return 0.

    For details, refer to the doctest.

    >>> put1 = kv()
    >>> get2, put2 = put1('cat', 'animal')
    >>> get3, put3 = put2('table', 'furniture')
    >>> get4, put4 = put3('cup', 'utensil')
    >>> get5, put5 = put4('thesis', 'paper')
    >>> get5('thesis')
    'paper'
    >>> get5('cup')
    'utensil'
    >>> get5('table')
    'furniture'
    >>> get5('cat')
    'animal'
    >>> get3('cup')
    0
    """
    def put(k, v):
        def get(k2):    # this get is recursive
            if k2 == k:
                return v
            else:
                return prev(k2) # calling previous gets with current values

        # to keep track of the previous get (state), return a new kv with the current get as param
        # this ensures that you can continue to put and and can get the prev get function to retrieve the key value pairs
        return get, kv(get)
    return put
    
# ORIGINAL SKELETON FOLLOWS

# def kv(prev=lambda x: 0):
#     """
#     A kv store is a store that associates keys with values.

#     To create a kv store, call the function `kv`, to get a `put` function.
#     This function enables you to "put" a key-value pair into the store, and
#     returns two functions `get` and another `put`. The `get` function should
#     let you look up a key and return its corresponding value, while the
#     new `put` function should let you continue adding on to the existing
#     kv store.

#     Note that you can assume that every key provided is unique. If you try to
#     get the value for a key that does not exist, return 0.

#     For details, refer to the doctest.

#     >>> put1 = kv()
#     >>> get2, put2 = put1('cat', 'animal')
#     >>> get3, put3 = put2('table', 'furniture')
#     >>> get4, put4 = put3('cup', 'utensil')
#     >>> get5, put5 = put4('thesis', 'paper')
#     >>> get5('thesis')
#     'paper'
#     >>> get5('cup')
#     'utensil'
#     >>> get5('table')
#     'furniture'
#     >>> get5('cat')
#     'animal'
#     >>> get3('cup')
#     0
#     """
#     the prev should be considered
#
#     def put(k, v):
#         def get(k2):
#             if ______:
#                 ______
#             else:
#                 ______
#         return get, put
#     need to find a way to keep check of prev and check if there is a value
#     return ______

#
