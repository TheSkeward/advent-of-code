"""2020 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.read().splitlines()
import re

VALID_COUNT = sum(
    (lowest <= word.count(letter) <= highest)
    for (lowest, highest, letter, word) in [
        [
            cast(var)
            for cast, var in zip(
                (int, int, str, str), re.match(r"(\d+)-(\d+) (.): (.+)", line).groups()
            )
        ]
        for line in open("input").read().splitlines()
    ]
)
VALID_COUNT_2 = sum(
    (word[first_position - 1] == letter) ^ (word[second_position - 1] == letter)
    for (first_position, second_position, letter, word) in [
        [
            cast(var)
            for cast, var in zip(
                (int, int, str, str), re.match(r"(\d+)-(\d+) (.): (.+)", line).groups()
            )
        ]
        for line in puzzle_input
    ]
)
print(VALID_COUNT, VALID_COUNT_2)