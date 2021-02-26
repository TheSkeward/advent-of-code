"""
2017 Advent of Code, Day 3
"""


def calculate(square):
    """Returns the number of steps required to carry the data
    from the specified square all the way to the access port"""
    steps = x = y = 0
    arm = current = 1
    face = ">"
    map_dict = {(0, 0): 1}
    step_dict = {">": (1, 0), "^": (0, 1), "<": (-1, 0), "v": (0, -1)}
    while current < int(square):
        if current < 810:
            print(x, y, current)
        x += step_dict[face][0]
        y += step_dict[face][1]
        current = 0
        for xadj in range(x - 1, x + 2):
            for yadj in range(y - 1, y + 2):
                if (xadj, yadj) in map_dict:
                    current += map_dict[(xadj, yadj)]
        map_dict[(x, y)] = current
        steps += 1
        if steps == arm:
            face = next_direction(face)
            arm += 1 if face in "<>" else 0
            steps = 0
    return current


def next_direction(s):
    directions = "v>^<"
    return directions[(directions.index(s) + 1) % 4]


with open("input", "r+") as file:
    puzzle_input = file.read()
    print(calculate(puzzle_input))
