"""2020 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.readlines()
ANSWER = 0
ANSWER_2 = 0
for index, entry in enumerate(puzzle_input):
    for second_index, second_entry in enumerate(puzzle_input):
        if (
            not ANSWER
            and int(puzzle_input[index]) + int(puzzle_input[second_index]) == 2020
        ):
            ANSWER = int(entry) * int(second_entry)
        for third_index, third_entry in enumerate(puzzle_input):
            if (
                not ANSWER_2
                and int(puzzle_input[index])
                + int(puzzle_input[second_index])
                + int(puzzle_input[third_index])
                == 2020
            ):
                ANSWER_2 = int(entry) * int(second_entry) * int(third_entry)
print(ANSWER, ANSWER_2)
