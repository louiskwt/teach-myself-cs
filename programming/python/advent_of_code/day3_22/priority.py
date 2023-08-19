import string

# priority dictionary        
weight_list = [i for i in range(1, 52+1)]
item_list = list(string.ascii_letters)
priority_dict = dict(zip(item_list, weight_list))

def sum_rucksack_priority(rucksacks):
    priority = 0
    for r in rucksacks:
        # c represents the compartments in the rucksack (r)
        c1 = r[len(r)//2:]
        c2 = r[:len(r)//2]
        duplicate = list(set(c1) & set(c2))
        priority += priority_dict[duplicate[0]]
    print(priority)

def sum_badge_priority(groups):
    shared_badge_priority = 0
    for group in groups:
        shared_badge = list(set(group[0]) & set(group[1]) & set(group[2]))
        shared_badge_priority += priority_dict[shared_badge[0]]

    print(shared_badge_priority)
   
try:
    trial_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ]

    trial_rucksack = [list(r) for r in trial_data]

    rucksack_data = open("input.txt", 'r').read().splitlines()
    rucksacks = [list(r) for r in rucksack_data]

    groups = [rucksack_data[i:i+3] for i in range(0, len(rucksack_data), 3)]
    trial_group = [trial_data[i:i+3] for i in range(0, len(trial_data), 3)]

    #Part 1
    sum_rucksack_priority(trial_rucksack) #157
    sum_rucksack_priority(rucksacks) #7785
    # Part 2
    sum_badge_priority(trial_group) #70
    sum_badge_priority(groups) # 2633
except:
    print("An error occurred")