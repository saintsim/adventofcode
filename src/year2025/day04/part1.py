#!/usr/bin/env python3

COORDS = {(-1, -1), (0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)}


def get_value(grid, row, col):
    if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1:
        return None
    else:
        return grid[row][col]


def can_access(grid, row, col):
    paper_count = 0
    for coord in COORDS:
        if get_value(grid, row+coord[0], col+coord[1]) == '@':
            paper_count += 1
    return paper_count < 4


def part1(input):
    grid = [list(i) for i in input.split("\n")]
    access_counter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if get_value(grid, row, col) == '@':
                access_counter += can_access(grid, row, col)
    return access_counter


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
