import string

try:
    # priority dictionary
    weight_list = [i for i in range(1, 52+1)]
    item_list = list(string.ascii_letters)
    priority_dict = dict(zip(item_list, weight_list))

    rucksack = open("input.txt", 'r').read().splitlines()
    rucksack_with_splited_items = [[*r] for r in rucksack]
    priority_lst = [priority_dict[item] for sublist in rucksack_with_splited_items for n, item in enumerate(sublist) if item in sublist[:n]]

    priority_sum = sum(priority_lst)
    print(priority_sum)
    
except:
    print("Error when loading file")