"""2016 Advent of Code, Day 1"""
with open("input", "r+") as file:
    puzzle_input = file.read()


def turn(facing, direction):
    """Returns the new facing given a cardinal facing and a left/right direction"""
    clockwise = "NESW"
    if direction == "L":
        facing = clockwise[(clockwise.index(facing) - 1) % 4]
    if direction == "R":
        facing = clockwise[(clockwise.index(facing) + 1) % 4]
    return facing


def forward(facing, x_axis, y_axis):
    """Returns the X and Y axis after stepping forward"""
    if facing == "N":
        x_axis += 1
    if facing == "S":
        x_axis -= 1
    if facing == "E":
        y_axis += 1
    if facing == "W":
        y_axis -= 1
    return x_axis, y_axis


def solve(command_list):
    """Returns the position of the first place visited twice"""
    # starting position
    facing, x_axis, y_axis = "N", 0, 0
    visited = []
    position = "No match found."
    for command in command_list:
        direction, steps = command[0], command[1:]
        facing = turn(facing, direction)
        for _ in range(int(steps)):
            x_axis, y_axis = forward(facing, x_axis, y_axis)
            if (x_axis, y_axis) in visited:
                position = abs(x_axis) + abs(y_axis)
                return position
            visited.append((x_axis, y_axis))
    return position


print(solve(puzzle_input.split(", ")))
