#!/usr/bin/env python3

from libraries.parsing.matrix import parse_matrix

MATRIX = []
WALL = '#'
DIRECTIONS = ['U', 'R', 'D', 'L']
DIRECTION_MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def off_map(position):
    return position[0] < 0 or position[0] > len(MATRIX)-1 or position[1] < 0 or position[1] > len(MATRIX[0])-1


def do_walk(walls, start, direction_index):
    current_position = start
    visited = set()
    visited.add(current_position)
    print(current_position)
    while True:
        next_move = (current_position[0]+DIRECTION_MOVES[direction_index][0],
                     current_position[1]+DIRECTION_MOVES[direction_index][1])
        if off_map(next_move):
            return visited
        if next_move in walls:
            # hit obstacle
            direction_index = (direction_index+1) % len(DIRECTION_MOVES)
        else:
            current_position = next_move
            print(current_position)
            visited.add(current_position)


def parse(input):
    global MATRIX
    MATRIX = parse_matrix(input)
    # record the map points
    walls = {}
    start = None
    direction_index = 0
    for idx_y, col in enumerate(MATRIX):
        for idx_x, row in enumerate(col):
            if row == '#':
                walls[(idx_y, idx_x)] = WALL
            elif row == "^":
                start = (idx_y, idx_x)
    visited = do_walk(walls, start, direction_index)
    return len(visited)


def part1(input):
    return parse(input)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
