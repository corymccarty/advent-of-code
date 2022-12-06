with open("2022/day_4/input.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

full_overlap_count = 0
partial_overlap_count = 0
for line in lines:
    assignments = line.split(",")
    elf1_bounds_strings = assignments[0].split("-")
    elf2_bounds_strings = assignments[1].split("-")
    elf1_start = int(elf1_bounds_strings[0])
    elf1_end = int(elf1_bounds_strings[1])
    elf1_assignment = set(range(elf1_start, elf1_end + 1))
    elf2_start = int(elf2_bounds_strings[0])
    elf2_end = int(elf2_bounds_strings[1])
    elf2_assignment = set(range(elf2_start, elf2_end + 1))
    if elf1_assignment.issubset(elf2_assignment) or elf1_assignment.issuperset(
        elf2_assignment
    ):
        full_overlap_count += 1
    if elf1_assignment.intersection(elf2_assignment):
        partial_overlap_count += 1


print(f"There are {full_overlap_count} fully overlapping assignments.")
print(f"There are {partial_overlap_count} partially overlapping assignments.")
