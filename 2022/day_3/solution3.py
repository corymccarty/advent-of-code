import string
from typing import List


def prioritize_item(item: str) -> int:
    return string.ascii_letters.index(item) + 1


with open("2022/day_3/input.txt") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

shared_items: List[str] = []

for line in lines:
    ruck_size = int(len(line) / 2)
    ruck1 = line[:ruck_size]
    ruck2 = line[ruck_size:]
    ruck1_items = set(ruck1)
    ruck2_items = set(ruck2)
    shared_item = list(ruck1_items.intersection(ruck2_items))[0]
    shared_items.append(shared_item)

shared_item_priorities = [prioritize_item(item) for item in shared_items]

print(f"Total Priority: {sum(shared_item_priorities)}")

badges: List[str] = []
num_groups = int(len(lines) / 3)
for index in range(num_groups):
    start_index = index * 3
    end_index = start_index + 3
    elves = lines[start_index:end_index]
    elf1 = set(elves[0])
    elf2 = set(elves[1])
    elf3 = set(elves[2])
    common = elf1.intersection(elf2).intersection(elf3)
    badge = list(common)[0]
    badges.append(badge)

badge_priorities = [prioritize_item(badge) for badge in badges]

print(f"Badge Priority: {sum(badge_priorities)}")
