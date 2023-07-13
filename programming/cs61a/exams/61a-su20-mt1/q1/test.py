from q1 import*

put1 = kv()
get2, put2 = put1('cat', 'animal')
get3, put3 = put2('table', 'furniture')
get4, put4 = put3('cup', 'utensil')
get5, put5 = put4('thesis', 'paper')

print(get5('thesis'))  #paper
print(get5('cup')) # utensil
print(get5('table')) #'furniture
print(get5('cat')) # animal
print(get3('cup')) # 0


