#!/usr/bin/env python3


def parse(input):
    locks = []
    keys = []
    for grid_input in input.split('\n\n'):
        grid = grid_input.split('\n')
        if '#' in grid[0]:
            locks.append(grid)
        else:
            keys.append(grid)
    return locks, keys


def get_heights(grid):
    heights = []
    for _ in range(len(grid[0])):
        heights.append(-1)
    for y_idx, row in enumerate(grid):
        for x_idx, cell in enumerate(list(row)):
            if cell == '#':
                heights[x_idx] += 1
    return heights


def calc_overlaps(lock_heights, key_heights, grid_height):
    total = 0
    pairs = []
    for key_idx, key in enumerate(key_heights):
        for lock_idx, lock in enumerate(lock_heights):
            match = True
            for i in range(len(key)):
                height_combined = key[i] + lock[i]
                if height_combined > grid_height-2:
                    match = False
                    break
            if match is True:
                pairs.append((lock, key))
    return len(pairs)


def part1(input):
    locks, keys = parse(input)
    lock_heights = []
    key_heights = []
    for lock in locks:
        heights = get_heights(lock)
        lock_heights.append(heights)
    for key in keys:
        heights = get_heights(key)
        key_heights.append(heights)
    return calc_overlaps(lock_heights, key_heights, len(locks[0]))


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
