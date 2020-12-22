"""2019 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()


def mass(item):
    """Calculate the fuel required for an item, and the fuel required for that fuel, and so on"""
    fuel = item // 3 - 2
    if fuel < 0:
        return 0
    return fuel + mass(fuel)


SUM = 0
SUM_2 = 0
for module in puzzle_input:
    SUM += int(module) // 3 - 2
    SUM_2 += mass(int(module))
print(SUM, SUM_2)
