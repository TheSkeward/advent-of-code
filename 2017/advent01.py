"""2017 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.read().strip("\n")
SUM = 0
SUM_2 = 0
for index, character in enumerate(puzzle_input):
    if character == puzzle_input[(index + 1) % len(puzzle_input)]:
        SUM += int(character)
    if (
        character
        == puzzle_input[(index + (len(puzzle_input) // 2)) % len(puzzle_input)]
    ):
        SUM_2 += int(character)
print(SUM, SUM_2)
