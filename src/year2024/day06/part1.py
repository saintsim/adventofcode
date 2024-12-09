#!/usr/bin/env python3

from libraries.parsing.matrix import parse_matrix

#                  'U',     'R',    'D',    'L'
DIRECTION_MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def off_map(matrix, position):
    return position[0] < 0 or position[0] > len(matrix)-1 or position[1] < 0 or position[1] > len(matrix[0])-1


def do_walk(matrix, walls, start, direction_index):
    current_position = start
    visited = set()
    visited.add(current_position)
    print(current_position)
    while True:
        next_move = (current_position[0]+DIRECTION_MOVES[direction_index][0],
                     current_position[1]+DIRECTION_MOVES[direction_index][1])
        if off_map(matrix, next_move):
            return visited
        if next_move in walls:
            # hit obstacle
            direction_index = (direction_index+1) % len(DIRECTION_MOVES)
        else:
            current_position = next_move
            print(current_position)
            visited.add(current_position)


def part1(input):
    matrix = parse_matrix(input)
    walls = {}
    start = None
    direction_index = 0 # starts up
    for idx_y, col in enumerate(matrix):
        for idx_x, row in enumerate(col):
            if row == '#':
                walls[(idx_y, idx_x)] = 1
            elif row == "^":
                start = (idx_y, idx_x)
    visited = do_walk(matrix, walls, start, direction_index)
    return len(visited)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
