#!/usr/bin/env python3

VISIBLE_GRID = None
GRID = []
GRID_SIZE = 0


def is_visible_for_direction(x, y, move_x, move_y):
    current_height = GRID[y][x]
    global VISIBLE_GRID
    while True:
        x += move_x
        y += move_y
        if x < 0 or y < 0 or x > GRID_SIZE-1 or y > GRID_SIZE-1:
            break
        next_height = GRID[y][x]
        if next_height >= current_height:
            return 0
    return 1


def is_visibile(x, y):
    print(x,y)
    if x == 0 or y == 0 or x == GRID_SIZE-1 or y == GRID_SIZE-1:
        return 1
    #       X   Y
    # up:   0   -1
    # down: 0   1
    # left  -1  0
    # right 1   0
    if is_visible_for_direction(x, y, 0, -1) or is_visible_for_direction(x, y, 0, 1) or is_visible_for_direction(x, y, -1, 0) or is_visible_for_direction(x, y, 1, 0):
        VISIBLE_GRID[y][x] = 1
        return 1
    return 0


def grid(input):
    global GRID_SIZE, VISIBLE_GRID
    GRID_SIZE = len(input[0])
    VISIBLE_GRID = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
    amount_visible = 0
    for line in input:
        GRID.append(list(line))
    for y, row in enumerate(GRID):
        for x, cell in enumerate(row):
            cell_visible = is_visibile(x, y)
            VISIBLE_GRID[y][x] = cell_visible
            amount_visible += cell_visible
    return amount_visible


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(grid(lines)))

