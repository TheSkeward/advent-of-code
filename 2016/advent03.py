"""
2016 Advent of Code, Day 3
"""


def calculate(tri_list):
    """Returns the number of valid triangles"""
    acc, a, b, c = 0, [], [], []
    for line in tri_list:
        coords = list(map(int, (line.split())))
        for i, triangle in enumerate((a, b, c)):
            triangle.append(coords[i])
        if len(a) == 3:
            for triangle in (a, b, c):
                triangle.sort()
                if triangle[0] + triangle[1] > triangle[2]:
                    acc += 1
            a, b, c = [], [], []
    return acc


with open("input", "r+") as file:
    puzzle_input = file.readlines()
print(calculate(puzzle_input))
