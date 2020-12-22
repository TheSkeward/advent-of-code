"""2018 Advent of Code, Day 2"""
with open("input", "r+") as file:
    puzzle_input = file.read().splitlines()
from collections import Counter

CHECKSUM = 0
CHECKSUM_2 = ""
EXACTLY_TWO = [0, False]
EXACTLY_THREE = [0, False]
for ID in puzzle_input:
    EXACTLY_TWO[1], EXACTLY_THREE[1] = False, False
    for letter, count in Counter(ID).items():
        if not EXACTLY_TWO[1] and count == 2:
            EXACTLY_TWO[0] += 1
            EXACTLY_TWO[1] = True
        if not EXACTLY_THREE[1] and count == 3:
            EXACTLY_THREE[0] += 1
            EXACTLY_THREE[1] = True
    for index in range(len(ID)):
        for second_ID in puzzle_input:
            if (
                not CHECKSUM_2
                and ID != second_ID
                and ID
                and ID[:index] + ID[index + 1 :]
                == second_ID[:index] + second_ID[index + 1 :]
            ):
                CHECKSUM_2 = ID[:index] + ID[index + 1 :]
CHECKSUM = EXACTLY_TWO[0] * EXACTLY_THREE[0]
print(CHECKSUM, CHECKSUM_2)
