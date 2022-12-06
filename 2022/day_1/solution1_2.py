with open("input1-1.txt", "r") as file:
    lines = file.readlines()

elves = []
current_elf_calories = 0
for line in lines:
    line = line.strip()
    if line == "":
        elves.append(current_elf_calories)
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

elves.sort()
print(elves)
print(sum(elves[-3:]))
