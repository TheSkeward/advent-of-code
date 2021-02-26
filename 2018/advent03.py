"""
2018 Advent of Code, Day 3
"""
from collections import defaultdict


def calculate(claims):
    """Returns the number of square inches within two or more claims"""
    ids = defaultdict(set)
    for line in claims:
        claim_id, placement, dimensions = (
            line.replace("#", "").replace("@", "").replace(":", "").split()
        )
        x, y = map(int, placement.split(","))
        w, h = map(int, dimensions.split("x"))
        for i in range(x + 1, w + x + 1):
            for j in range(y + 1, h + y + 1):
                ids[(i, j)].add(int(claim_id))
    part1_ans = sum([1 for coord in ids if len(ids[coord]) > 1])
    to_be_deleted = set()
    unique_claims = set()
    for claim in ids.values():
        for elem in claim:
            if len(claim) > 1:
                to_be_deleted.add(elem)
            unique_claims.add(elem)
    unique_claims -= to_be_deleted
    part2_ans = unique_claims.pop()
    return part1_ans, part2_ans


with open("input", "r+") as file:
    puzzle_input = file.readlines()
    print(calculate(puzzle_input))
