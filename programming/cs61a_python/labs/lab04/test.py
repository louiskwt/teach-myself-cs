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

from lab04 import*
# berkeley = make_city('Berkeley', 37.87, 112.26)
#stanford = make_city('Stanford', 34.05, 118.25)
#test_1 = closer_city(38.33, 121.44, berkeley, stanford)
#print(test_1) # Stanford

#bucharest = make_city('Bucharest', 44.43, 26.10)
#vienna = make_city('Vienna', 48.20, 16.37)
#test_2 = closer_city(41.29, 174.78, bucharest, vienna)
#print(test_2) # Bucharest

print(add_chars("owl", "howl"))
print(add_chars("want", "wanton"))
print(add_chars("rat", "radiate"))
