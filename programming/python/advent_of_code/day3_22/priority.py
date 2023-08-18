import string

# priority dictionary        
weight_list = [i for i in range(1, 52+1)]
item_list = list(string.ascii_letters)
priority_dict = dict(zip(item_list, weight_list))


def sum_priority(rucksacks):
    try:
        dup = []
        for r in rucksacks:
            # c represents the compartments in the rucksack (r)
            c1 = r[len(r)//2:]
            c2 = r[:len(r)//2]
            d = set(c1) & set(c2)
            for i in d:
                dup.append(priority_dict[i])
    except:
        print("An error occurred")


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

sum_priority(trial_rucksack) #157
sum_priority(rucksacks) #7785


