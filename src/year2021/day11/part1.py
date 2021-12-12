#!/usr/bin/env python3

def parse(input):
    return [[int(i) for i in line] for line in input]


def energy_level_increase(grid, increase_amount):
    return [[i+increase_amount for i in line] for line in grid]


def update_octopus(grid, x, y):
    if 0 <= y <= len(grid)-1 and 0 <= x <= len(grid[0])-1:
        if grid[y][x] != 0:
            grid[y][x] += 1
    return grid


def energy_level_increase_neighbours(grid, x, y):
    # --> x
    # | A B C
    # | D X E
    # y F G H
    for x_adj in range(-1, 2):
        for y_adj in range(-1, 2):
            if x_adj == 0 and y_adj == 0:
                continue
            grid = update_octopus(grid, x+x_adj, y+y_adj)
    return grid


def flash_check(grid):
    #  anyone >9 to flash
    updated_grid = []
    flashes = []
    for y, line in enumerate(grid):
        updated_line = []
        for x, octopus in enumerate(line):
            if octopus > 9:
                octopus = 0
                flashes.append((x,y))
            updated_line.append(octopus)
        updated_grid.append(updated_line)
    return updated_grid, flashes


def flash_time(grid):
    flash_count = 0
    while True:
        grid, flashes = flash_check(grid)
        if len(flashes):
            flash_count += len(flashes)
            for flash in flashes:
                grid = energy_level_increase_neighbours(grid, flash[0], flash[1])
        else:
            break
    return grid, flash_count


def print_grid(grid):
    for line in grid:
        print(line)


def total_flashes(input, steps):
    grid = parse(input)
    flash_count = 0
    for step in range(steps):
        print("Step: " + str(step))
        grid = energy_level_increase(grid, 1)
        grid, step_flash_count = flash_time(grid)
        flash_count += step_flash_count
        print_grid(grid)
    return flash_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(total_flashes(lines, 100)))
