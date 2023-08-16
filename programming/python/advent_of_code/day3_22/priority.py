import string

try:
    # priority dictionary
    weight_list = [i for i in range(1, 52+1)]
    item_list = list(string.ascii_letters)
    priority_dict = dict(zip(item_list, weight_list))

    rucksack = open("input.txt", 'r').read().splitlines()
    rucksack_with_splited_items = [[*r] for r in rucksack]

    trial_data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    ]
    trial_rucksack = [list(r) for r in trial_data]
    trial_priority_lst = [priority_dict[item] for sublist in trial_rucksack for n, item in enumerate(sublist) if item in sublist[:n]]

    print(trial_priority_lst)

    dup = []
    for r in trial_rucksack:
        c1 = r[len(r)//2:]
        c2 = r[:len(r)//2]
        dup.append(set(c1) & set(c2))
    
    print([s for s in dup])
    
        
    

    # print(dup)

    # priority_sum = sum(priority_lst)
    # print(priority_sum)
    
except:
    print("Error when loading file")