#!/usr/bin/env python3

import re

BOARD = dict()
POSSIBLE_DIRECTIONS = ['R', 'D', 'L', 'U']
MOVE_MAP = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}


def wrap_around(current_pos, next_pos):
    # which direction to wrap
    if current_pos[0] == next_pos[0]:
        # wrap left or right
        if next_pos[1] > current_pos[1]:
            # trying to move down
            smallest_y = 100
            for key in BOARD.keys():
                if key[0] == next_pos[0] and key[1] < smallest_y:
                    smallest_y = key[1]
            wrap = next_pos[0], smallest_y
        else:
            # trying to move up
            biggest_y = 0
            for key in BOARD.keys():
                if key[0] == next_pos[0] and key[1] > biggest_y:
                    biggest_y = key[1]
            wrap = next_pos[0], biggest_y
    else:
        # wrap up or down
        if next_pos[0] > current_pos[0]:
            # trying to move right
            smallest_x = 100
            for key in BOARD.keys():
                if key[1] == next_pos[1] and key[0] < smallest_x:
                    smallest_x = key[0]
            wrap = smallest_x, next_pos[1]
        else:
            # trying to move left
            biggest_x = 0
            for key in BOARD.keys():
                if key[1] == next_pos[1] and key[0] > biggest_x:
                    biggest_x = key[0]
            wrap = biggest_x, next_pos[1]
    if BOARD[wrap] == '#':
        return current_pos
    else:
        return wrap


def add_tuples(t1, t2):
    return tuple(map(lambda x, y: x + y, t1, t2))


def follow_directions(directions, first_pos):
    current_pos = first_pos
    direction_ix = 0
    for direction in directions:
        if direction.isnumeric():
            # move this amount
            for i in range(int(direction)):
                next_pos = add_tuples(current_pos, MOVE_MAP[POSSIBLE_DIRECTIONS[direction_ix]])
                if next_pos in BOARD:
                    if BOARD[next_pos] == '#':
                        # cannot move, exit
                        continue
                    else:
                        current_pos = next_pos
                else:
                    current_pos = wrap_around(current_pos, next_pos)
        else:
            # turn this direction (L or R)
            if direction == 'R':
                direction_ix = (direction_ix+1) % len(POSSIBLE_DIRECTIONS)
            else:
                direction_ix = (direction_ix-1) % len(POSSIBLE_DIRECTIONS)
    final_pos = current_pos[0]+1, current_pos[1]+1
    print('Final pos => ', final_pos)
    print('Final facing => ', direction_ix)
    return (1000*final_pos[1]) + (4*final_pos[0]) + direction_ix


def maze(input):
    board_in, directions_in = input.split('\n\n')
    board_matrix = board_in.split('\n')
    first_pos = None
    for y, row in enumerate(board_matrix):
        for x, cell in enumerate(row):
            if cell != " ":
                if first_pos is None:
                    first_pos = (x,y)
                BOARD[(x, y)] = cell
    directions = re.split('(L|R)', directions_in)
    final_score = follow_directions(directions, first_pos)
    return final_score


if __name__ == '__main__':
    with open('input', 'r') as file:
         print('Result: ' + str(maze(file.read())))