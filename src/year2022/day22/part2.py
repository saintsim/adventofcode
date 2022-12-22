#!/usr/bin/env python3

import re

BOARD = dict()
POSSIBLE_DIRECTIONS = ['R', 'D', 'L', 'U']
MOVE_MAP = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}


def find_group(pos):
    width = 50
    # top section (1 or 2)
    if pos[1] < width:
        if pos[0] < (width*2):
            return 1
        else:
            return 2
    elif pos[1] < (width*2):
        return 3
    elif pos[1] < (width*3):
        # 4 or 5
        if pos[0] < width:
            return 4
        else:
            return 5
    else:
        return 6


def wrap_around(current_pos, next_pos, direction_ix):
    # which direction to wrap
    group = find_group(current_pos)
    if current_pos[0] == next_pos[0]:
        if next_pos[1] > current_pos[1]:
            # trying to move down
            if group == 6:
                # going to face 2
                wrap = current_pos[0]+100, 0
                wrap_direction_ix = 1  # down
            elif group == 5:
                # going to face 6
                wrap = 49, current_pos[0]+100  # -50 + 150
                wrap_direction_ix = 2  # left
            else:  # 2
                # going to face 3 left
                wrap = 99, current_pos[0]-50  # -100, +50
                wrap_direction_ix = 2  # left
        else:
            # trying to move up
            if group == 4:
                # to 3 right
                wrap = 50, current_pos[0]+50
                wrap_direction_ix = 0  # right
            elif group == 1:
                # to 6 right
                wrap = 0, current_pos[0]+100  # -50, +150
                wrap_direction_ix = 0  # right
            else:  # 2
                # to 6 up
                wrap = current_pos[0]-100, 199  # -100
                wrap_direction_ix = 3  # up
    else:
        if next_pos[0] > current_pos[0]:
            # trying to move right
            if group == 2:
                # to 5 bottom
                wrap = 99, 149-current_pos[1]
                wrap_direction_ix = 2  # left
            elif group == 3:
                # to 2 up
                wrap = current_pos[1]+50, 49  # -50, +100
                wrap_direction_ix = 3  # up
            elif group == 5:
                # to 2 left
                wrap = 149, 149-current_pos[1]
                wrap_direction_ix = 2  # left
            else:  # 6
                # to 5 up
                wrap = current_pos[1]-100, 149  # -150, +50
                wrap_direction_ix = 3  # up
        else:
            # trying to move left
            if group == 1:
                # to 4 right
                wrap = 0, 149-current_pos[1]
                wrap_direction_ix = 0  # right
            elif group == 3:
                # to 4 down
                wrap = current_pos[1]-50, 100  # -50
                wrap_direction_ix = 1  # down
            elif group == 4:
                # to 1 right
                wrap = 50, 149-current_pos[1]
                wrap_direction_ix = 0  # right
            else:  # 6
                # to 1 down
                wrap = current_pos[1]-100, 0  # -150, +50
                wrap_direction_ix = 1  # down
    if BOARD[wrap] == '#':
        return current_pos, direction_ix
    else:
        return wrap, wrap_direction_ix


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
                        break
                    else:
                        current_pos = next_pos
                else:
                    current_pos, direction_ix = wrap_around(current_pos, next_pos, direction_ix)
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
