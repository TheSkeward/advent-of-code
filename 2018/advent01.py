"""2018 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()
SUM = 0
TOTAL = 0
FREQUENCY = 0
REACHED = set()
MATCH = False
ONCE_THROUGH = False
while not MATCH or not ONCE_THROUGH:
    for number in list(map(int, puzzle_input)):
        if not MATCH and SUM in REACHED:
            MATCH = True
            FREQUENCY = SUM
        REACHED.add(SUM)
        SUM += number
    if not ONCE_THROUGH:
        ONCE_THROUGH = True
        TOTAL = SUM


print(TOTAL, FREQUENCY)
