from collections import namedtuple
from typing import Dict, List


Instruction = namedtuple("Instruction", ["source", "destination", "quantity"])


with open("2022/day_5/input.txt") as file:
    lines = file.readlines()
lines = [line.strip("\n") for line in lines]

cargo_lines: List[str] = []
instructions: List[Instruction] = []

processing_cargo = True
for line in lines:
    if processing_cargo:
        if line == "":
            processing_cargo = False
        else:
            cargo_lines.append(line)
    else:
        words = line.split()
        quantity = int(words[1])
        source = int(words[3])
        destination = int(words[5])
        instructions.append(Instruction(source, destination, quantity))

stack_number_line = cargo_lines.pop()
stack_index_range = range(1, len(stack_number_line), 4)
stack_number_range = range(1, len(stack_index_range) + 1)
stacks: Dict[int, List[str]] = {}

# Initialize the stacks
stack_numbers: List[int] = []
for index in stack_index_range:
    stack_number = int(stack_number_line[index])
    stacks[stack_number] = []
    stack_numbers.append(stack_number)

# Parse the cargo into the stacks
while len(cargo_lines) > 0:
    line = cargo_lines.pop()
    for index, number in zip(stack_index_range, stack_number_range):
        cargo = line[index]
        if cargo != " ":
            stacks[number].append(cargo)

for instruction in instructions:
    for _ in range(instruction.quantity):
        stacks[instruction.destination].append(stacks[instruction.source].pop())

stack_tops = ""
for stack_number in stack_numbers:
    stack_tops += stacks[stack_number][-1]

print(f"Stack tops: {stack_tops}")
