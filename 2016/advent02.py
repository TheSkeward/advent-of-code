"""2016 Advent of Code, Day 2"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()
POSITION_1 = 5
POSITION_2 = 5
CODE = []
CODE_2 = []
TEST = []
for digit in puzzle_input:
    for instruction in digit:
        if instruction == "U":
            POSITION_1 -= 3 if POSITION_1 - 3 > 0 else 0
            POSITION_2 -= (
                0
                if POSITION_2 in [1, 2, 4, 5, 9]
                else 2
                if POSITION_2 in [3, 13]
                else 4
            )
        if instruction == "D":
            POSITION_1 += 3 if POSITION_1 + 3 < 10 else 0
            POSITION_2 += (
                0
                if POSITION_2 in [5, 9, 10, 12, 13]
                else 2
                if POSITION_2 in [1, 11]
                else 4
            )
        if instruction == "L":
            POSITION_1 -= 1 if POSITION_1 % 3 != 1 else 0
            POSITION_2 -= 0 if POSITION_2 in [1, 2, 5, 10, 13] else 1
        if instruction == "R":
            POSITION_1 += 1 if POSITION_1 % 3 != 0 else 0
            POSITION_2 += 0 if POSITION_2 in [1, 4, 9, 12, 13] else 1
    CODE.append(str(POSITION_1))
    CODE_2.append(str(hex(POSITION_2))[2:])
    TEST.append(POSITION_2)
CODE = "".join(CODE)
CODE_2 = "".join(CODE_2).upper()
print(CODE, CODE_2)
