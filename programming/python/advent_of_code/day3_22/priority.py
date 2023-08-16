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
        # c represents the compartment in the rucksack (r)
        c1 = r[len(r)//2:]
        c2 = r[:len(r)//2]
        d = set(c1) & set(c2)
        for i in d:
            dup.append(priority_dict[i])
    
    print(sum(dup))

except:
    print("Error when loading file")