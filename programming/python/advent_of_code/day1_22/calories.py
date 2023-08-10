elfs = open('input.txt').read().split("\n\n")

print(len(elfs))

cleaned_elfs = [e.split("\n") for e in elfs]
elfs_lst = []

for elf in cleaned_elfs:
    elfs_lst.append([int(c) for c in elf if c != ''])

max_cal = 0
elf_index = 0

for index, elf in enumerate(elfs_lst):
    total_cal = sum(elf)
    if total_cal > max_cal:
        elf_index = index
        max_cal = total_cal

print(elf, max_cal) 

# max_cal = 67450
