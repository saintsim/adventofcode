#!/usr/bin/env python3

DIRECTIONS = {
                '<': (0, -1),
                'v': (1, 0),
                '>': (0, 1),
                '^': (-1, 0)
            }
WALL = '#'
CURRENT_POSITION = '@'
EMPTY_CELL = '.'
BOX = 'O'


def parse(input):
    grid_input, moves_input = input.split('\n\n')
    start = None
    grid = []
    for y_idx, line in enumerate(grid_input.split('\n')):
        row = list(line)
        if CURRENT_POSITION in row:
            start = (y_idx, row.index(CURRENT_POSITION))
        grid.append(row)
    moves = list(moves_input)
    return grid, moves, start


def box_move(grid, next_move, next_direction, current):
    # box case
    # is next place free to move the box too
    after_next_move = next_move
    # between here and the wall is there a free cell before a wall
    while True:
        proposed_move = (after_next_move[0] + next_direction[0], after_next_move[1] + next_direction[1])
        proposed_move_grid_piece = grid[proposed_move[0]][proposed_move[1]]
        if proposed_move_grid_piece == WALL:
            # no action
            break
        elif proposed_move_grid_piece == BOX:
            after_next_move = proposed_move
            continue
        else:
            # empty!
            grid[current[0]][current[1]] = EMPTY_CELL
            grid[next_move[0]][next_move[1]] = CURRENT_POSITION
            grid[proposed_move[0]][proposed_move[1]] = BOX
            current = next_move
            break
    return current, grid


def run_moves(grid, moves, start):
    current = start
    for move in moves:
        if move == '\n':
            continue
        if move not in DIRECTIONS:
            pass
        next_direction = DIRECTIONS[move]
        next_move = (current[0] + next_direction[0], current[1] + next_direction[1])
        grid_piece = grid[next_move[0]][next_move[1]]
        if grid_piece == EMPTY_CELL:
            grid[current[0]][current[1]] = EMPTY_CELL
            grid[next_move[0]][next_move[1]] = CURRENT_POSITION
            current = next_move
            continue
        elif grid_piece == WALL:
            continue
        else:
            current, grid = box_move(grid, next_move, next_direction, current)
    return grid


def calc_gps(grid):
    total = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == BOX:
                total += ((y*100) + x)
    return total


def part1(input):
    grid, moves, start = parse(input)
    updated_grid = run_moves(grid, moves, start)
    return calc_gps(updated_grid)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
