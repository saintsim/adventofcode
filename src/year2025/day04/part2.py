#!/usr/bin/env python3

COORDS = {(-1, -1), (0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)}
GRID = []


def get_value(grid, row, col):
    if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1:
        return None
    else:
        return GRID[row][col]


def can_access(grid, row, col):
    paper_count = 0
    for coord in COORDS:
        if get_value(grid, row+coord[0], col+coord[1]) == '@':
            paper_count += 1
    return paper_count < 4


def part2(input):
    global GRID
    GRID = [list(i) for i in input.split("\n")]
    counter = 0
    while True:
        new_count = run_round()
        if new_count == 0:
            return counter
        else:
            counter += new_count


def run_round() -> int:
    access_counter = 0
    access_cells = []
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            if get_value(GRID, row, col) == '@':
                if can_access(GRID, row, col):
                    access_cells.append((row, col))
                    access_counter += 1
    for cell in access_cells:
        GRID[cell[0]][cell[1]] = 'x'
    return access_counter


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
