def find_duplicated_pair(lst):
    count = 0
    for pair in lst:
        if all(section in pair[0] for section in pair[1]) or all(section in pair[1] for section in pair[0]):
            count += 1
    return count

def find_overlapped_pair(lst):
    count = 0
    for pair in lst:
        overlapped = [s for s in pair[0] if s in pair[1]]
        if len(overlapped) >= 1:
            count += 1
    return count

try:
    assignment_list = open("input.txt", "r").read().splitlines()
    assignment_list = [group.split(",") for group in assignment_list]
    formatted_assignment_list = []
    for lst in assignment_list:
        section_range = [list(range(int(section.split("-")[0]), int(section.split("-")[1]) + 1)) for section in lst ]
        formatted_assignment_list.append(section_range)

    print(find_duplicated_pair(formatted_assignment_list)) # 560
    print(find_overlapped_pair(formatted_assignment_list)) # 839
except:
    print("Fail to process")