try:
    assignment_list = open("input.txt", "r").read().splitlines()
    assignment_list = [group.split(",") for group in assignment_list]
    formatted_assignment_list = []
    for lst in assignment_list:
        section_range = [list(range(int(section.split("-")[0]), int(section.split("-")[1]) + 1)) for section in lst ]
        formatted_assignment_list.append(section_range)
    print(formatted_assignment_list)
except:
    print("Fail to process")