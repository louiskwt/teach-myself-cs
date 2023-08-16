try:
    rucksack = open("input.txt", 'r').read().splitlines()
    rucksack_with_splited_items = [[*r] for r in rucksack]
    print(rucksack_with_splited_items)
    
except:
    print("Error when loading file")