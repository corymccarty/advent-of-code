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

read_outcome_map = {
    "X": Outcome.LOSS,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}


def get_required_shape(theirs: str, desired_outcome: Outcome) -> str:
    for round, outcome in outcome_map.items():
        if round.theirs == theirs and outcome == desired_outcome:
            return round.mine
    raise Exception("Not found")


with open("input2-1.txt") as file:
    lines = file.readlines()

total_score = 0
for line in lines:
    raw_round = line.strip().split()
    theirs = raw_round[0]
    desired_outcome = read_outcome_map[raw_round[1]]
    mine = get_required_shape(theirs, desired_outcome)
    total_score += score_map[mine]  # shape score
    total_score += desired_outcome.value  # outcome score

print(f"Total score is {total_score}")
