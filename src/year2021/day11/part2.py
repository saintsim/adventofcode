#!/usr/bin/env python3

from part1 import parse, energy_level_increase, flash_time, print_grid


def total_flashes(input, steps):
    grid = parse(input)
    flash_count = 0
    for step in range(steps):
        print("Step: " + str(step))
        grid = energy_level_increase(grid, 1)
        grid, step_flash_count = flash_time(grid)
        if step_flash_count == (len(grid)*len(grid[0])):
            return step+1
        flash_count += step_flash_count
        print_grid(grid)
    return None


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(total_flashes(lines, 100000)))
