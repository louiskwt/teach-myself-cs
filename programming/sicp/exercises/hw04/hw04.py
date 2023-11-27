def filter(condition, lst):
    """Filters lst with condition using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    el_to_pop = []
    for e in lst:
        if not condition(e):
            el_to_pop.append(e)
    
    for e in el_to_pop:
        index = lst.index(e)
        lst.pop(index)


def deep_map_mut(func, lst):
    """Deeply maps a function over a list, replacing each item
    in the original list object.
    Does NOT return the mutated list object.

    >>> l = [1, 2, [3, [4], 5], 6]
    >>> deep_map_mut(lambda x: x * x, l)
    >>> l
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map_mut(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"
    def mut_helper(el):
        if type(el) == list:
            for e in el:
                index = el.index(e)
                el[index] = mut_helper(e)
            return el
        else:
            return func(el) 
     
    for el in lst:
        index = lst.index(el)
        mutated_el = mut_helper(el)
        lst[index] = mutated_el


HW_SOURCE_FILE=__file__


def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
    def path_sum(p):
        b_label = label(p)
        if is_leaf(p):
            return b_label
        
        node_sums = []
        for node in branches(p):
            sum = b_label + path_sum(node)
            node_sums.append(sum)

        return max(node_sums)
    
    origin = label(t)
    path_sums = []

    for b in branches(t):
        p_sum = origin + path_sum(b)
        path_sums.append(p_sum)
    
    return max(path_sums)
    

HW_SOURCE_FILE=__file__


def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    def find_matches(b, m):
        if len(m) == len(word):
            return []
        
        matches = []
        b_label = label(b)

        if b_label in word:
            matches.append(b_label)
        
        if is_leaf(b):
            return matches

        for n in branches(b):
            matches = matches + find_matches(n, matches)

        return matches        

    matches = []
    t_label = label(t)
    if t_label in word:
        matches.append(t_label)

    if len(matches) == len(word):
        return True    

    for b in branches(t):
        matches = matches + find_matches(b, matches)
    
    return len(matches) == len(word) and matches[0] == t_label   
            



# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

