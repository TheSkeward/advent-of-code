"""
2015 Advent of Code, Day 1
"""
with open("input", "r+") as file:
    puzzle_input = file.read()
FLOOR = 0
POSITION = 0
BASEMENT = False
for (index, character) in enumerate(puzzle_input):
    if character == "(":
        FLOOR += 1
    if character == ")":
        FLOOR -= 1
    if not BASEMENT and FLOOR < 0:
        BASEMENT = True
        POSITION = index + 1
print(FLOOR, POSITION)
