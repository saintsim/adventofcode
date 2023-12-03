#!/usr/bin/env python3

LIFT_MAZE = []
ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]


def parse(input):
    lines = input.split('\n')
    for line in lines:
        maze_line = []
        for token in line:
            maze_line.append(token)
        LIFT_MAZE.append(maze_line)


def is_symbol_cell(point):
    if point[0] < 0 or point[1] < 0 or point[0] >= len(LIFT_MAZE) or point[1] >= len(LIFT_MAZE[0]):
        # off grid
        return False
    maze_point = LIFT_MAZE[point[0]][point[1]]
    if maze_point.isdigit() or maze_point == '.':
        return False
    return True


def is_adjacent_symbol(coord):
    for adj_coord in ADJACENT:
        new_point = (adj_coord[0]+coord[0], adj_coord[1]+coord[1])
        if is_symbol_cell(new_point):
            return True
    return False


def is_valid_part(x, y, length):
    # x and y is for the last number, so let's compute all x,y's
    coords = [(x, y)]
    if length > 1:
        for i in range(length-1):
            coords.append((x, y-i-1))
    for coord in coords:
        if is_adjacent_symbol(coord):
            return True
    return False


def get_part_numbers():
    valid_parts = []
    for x, line in enumerate(LIFT_MAZE):
        # find a sequence of numbers, then we can check if valid
        digits = ''
        for y, token in enumerate(line):
            if token.isdigit():
                digits += token
            else:
                if digits:
                    if is_valid_part(x, y-1, len(digits)):
                        valid_parts.append(int(digits))
                    digits = ''
        if digits:
            if is_valid_part(x, len(line) - 1, len(digits)):
                valid_parts.append(int(digits))
    return valid_parts


def lift(input):
    parse(input)
    res = get_part_numbers()
    print(res)
    return sum(res)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(lift(file.read())))
