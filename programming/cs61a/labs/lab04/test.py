def myfunc():
    """
    """

# summing recursive list
def lst_sum(lst):
    # another D&Q algorithms

    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    last_item = lst.pop()
    if type(last_item) is list:
        sum = last_item.pop() + lst_sum(last_item)
        return sum + lst_sum(lst)
    
    return last_item + lst_sum(lst)

                                                                            
