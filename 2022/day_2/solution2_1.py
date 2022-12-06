from collections import namedtuple
from enum import Enum


Round = namedtuple("Round", ["theirs", "mine"])


score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


outcome_map = {
    Round("A", "X"): Outcome.DRAW,
    Round("A", "Y"): Outcome.WIN,
    Round("A", "Z"): Outcome.LOSS,
    Round("B", "X"): Outcome.LOSS,
    Round("B", "Y"): Outcome.DRAW,
    Round("B", "Z"): Outcome.WIN,
    Round("C", "X"): Outcome.WIN,
    Round("C", "Y"): Outcome.LOSS,
    Round("C", "Z"): Outcome.DRAW,
}

with open("input2-1.txt") as file:
    lines = file.readlines()

total_score = 0
for line in lines:
    raw_round = line.strip().split()
    round = Round(raw_round[0], raw_round[1])
    total_score += score_map[round.mine]  # shape score
    total_score += outcome_map[round].value  # outcome score

print(f"Total score is {total_score}")
