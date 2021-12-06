#!/usr/bin/env python3

import re


def parse(input):
    lines = []
    max_x = 0
    max_y = 0
    for input_row in input:
        x1, y1, x2, y2 = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', input_row).groups()
        max_x = max(max_x, int(x1), int(x2))
        max_y = max(max_y, int(y1), int(y2))
        lines.append([(int(x1),int(y1)),(int(x2), int(y2))])
    return max_x, max_y, lines


def get_line_cells(line, include_diags):
    if not include_diags:
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
            print('skip: ' + str(line))
            return []
    line_cells = set(line)
    # increase or decrease y, keep x constant
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    x = x1
    y = y1
    if x1 != x2 and y1 != y2:
        # diagonal case
        while x != x2 and y != y2:
            x = x + 1 if x2 > x1 else x - 1
            y = y + 1 if y2 > y1 else y - 1
            line_cells.add((x,y))
    else:
        if x1 == x2:
            while y != y2:
                y = y + 1 if y2 > y1 else y - 1
                line_cells.add((x, y))
        else:
            while x != x2:
                x = x + 1 if x2 > x1 else x - 1
                line_cells.add((x, y))
    return line_cells


def add_line_to_grid(grid, line, include_diags):
    line_cells = get_line_cells(line, include_diags)
    for line_cell in line_cells:
        grid[line_cell[1]][line_cell[0]] += 1
    return grid


def number_of_overlaps(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                count += 1
    return count


def draw_grid(x_size, y_size, lines, include_diags):
    big_dimension = max(x_size, y_size)+1
    grid = [[0]*big_dimension for _ in range(big_dimension)]
    for line in lines:
        print(str(line))
        grid = add_line_to_grid(grid, line, include_diags)
    return number_of_overlaps(grid)


if __name__ == '__main__':
    with open('input', 'r') as file:
        max_x, max_y, lines = parse(file.readlines())
        print('Result: ' + str(draw_grid(max_x, max_y, lines, False)))
