"""2017 Advent of Code, Day 2"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()
SPREADSHEET = []
CHECKSUM = 0
CHECKSUM_2 = 0
for row in puzzle_input:
    SPREADSHEET.append([int(value) for value in row.strip().split()])
for row in SPREADSHEET:
    row.sort()
    CHECKSUM += row[-1] - row[0]
    for index, value in enumerate(row):
        for second_index, second_value in enumerate(row):
            if index != second_index and not value % second_value:
                CHECKSUM_2 += value // second_value

print(CHECKSUM, CHECKSUM_2)