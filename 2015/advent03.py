"""
2015 Advent of Code, Day 3
"""


def calculate(puzzle_input):
    """Tracks Santa's steps"""
    x = y = rx = ry = 0
    visited = set()
    robot = False
    for step in puzzle_input:
        if step == "^":
            if robot:
                ry += 1
            else:
                y += 1
        elif step == "v":
            if robot:
                ry -= 1
            else:
                y -= 1
        elif step == "<":
            if robot:
                rx -= 1
            else:
                x -= 1
        elif step == ">":
            if robot:
                rx += 1
            else:
                x += 1
        if robot:
            visited.add((rx, ry))
            robot = False
        else:
            visited.add((x, y))
            robot = True
    return len(visited)


with open("input", "r+") as file:
    puzzle_input = file.read()
print(calculate(puzzle_input))
