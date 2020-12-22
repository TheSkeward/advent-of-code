"""2015 Advent of Code, Day 2"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()
FEET = 0
FEET_2 = 0
for present in puzzle_input:
    l, w, h = list(map(int, present.split("x")))
    dimensions = [l, w, h]
    dimensions.sort()
    FEET += (2 * l * w) + (2 * w * h) + (2 * h * l) + min((l * w), (w * h), (h * l))
    FEET_2 += (dimensions[0] * 2) + (dimensions[1] * 2) + (l * w * h)
print(FEET, FEET_2)