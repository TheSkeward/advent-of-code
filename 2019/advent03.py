"""
2019 Advent of Code, Day 3
"""
from collections import defaultdict


def calculate(wires):
    """Returns the Manhattan distance from the central port to the closest intersection
    and the fewest combined steps the wires must take to reach an intersection"""
    occupied = defaultdict(set)
    steps_trace = dict()
    dir_dict = {"U": (0, 1), "L": (-1, 0), "R": (1, 0), "D": (0, -1)}
    for i, wire in enumerate(wires, 1):
        x = y = steps = 0
        twists = wire.strip().split(",")
        for twist in twists:
            for _ in range(int(twist[1:])):
                steps += 1
                x += dir_dict[twist[0]][0]
                y += dir_dict[twist[0]][1]
                occupied[(x, y)].add(i)
                steps_trace.setdefault((x, y, i), steps)
    if (0, 0) in occupied:
        del occupied[(0, 0)]
    if (0, 0) in steps_trace:
        del steps_trace[(0, 0)]
    part1_ans = part2_ans = float("inf")
    for coord, wires in occupied.items():
        if len(wires) > 1:
            part1_ans = min(part1_ans, abs(coord[0]) + abs(coord[1]))
            part2_ans = min(
                part2_ans,
                steps_trace[(coord[0], coord[1], 1)]
                + steps_trace[(coord[0], coord[1], 2)],
            )
    return part1_ans, part2_ans


with open("input", "r+") as file:
    puzzle_input = file.readlines()
    print(calculate(puzzle_input))
