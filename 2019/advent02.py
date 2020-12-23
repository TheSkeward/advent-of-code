"""2019 Advent of Code, Day 2"""
with open("input", "r+") as file:
    puzzle_input = file.read()
PROGRAM = list(map(int, puzzle_input.split(",")))


def process_opcode(program, opcode):
    """process opcodes according to instructions"""
    if program[opcode] == 1:
        program[program[opcode + 3]] = (
            program[program[opcode + 1]] + program[program[opcode + 2]]
        )
    elif program[opcode] == 2:
        program[program[opcode + 3]] = (
            program[program[opcode + 1]] * program[program[opcode + 2]]
        )
    elif program[opcode] == 99:
        return program
    return process_opcode(program, opcode + 4)


VALUE = process_opcode([PROGRAM[0]] + [12, 2] + PROGRAM[3:], 0)[0]
VALUE_2 = 0
for noun in range(100):
    for verb in range(100):
        if (
            not VALUE_2
            and process_opcode([PROGRAM[0]] + [noun, verb] + PROGRAM[3:], 0)[0]
            == 19690720
        ):
            VALUE_2 = 100 * noun + verb
print(VALUE, VALUE_2)
