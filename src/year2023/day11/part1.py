#!/usr/bin/env python3

from collections import defaultdict


def find_indices(list_to_check, item_to_find):
    return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]


def galaxy_expansion(world):
    x_index_to_expand = []
    y_index_to_expand = [True] * len(world[0])
    for idx, x in enumerate(world):
        if '#' not in x:
            x_index_to_expand.append(idx)
        for idx_match in find_indices(x, '#'):
            y_index_to_expand[idx_match] = False
    # rows (x)
    for i, idx in enumerate(x_index_to_expand):
        world.insert(i+idx+1, ['.']*len(world[0]))
    # cols (y)
    for idx, x in enumerate(world):
        hit = 0
        for idx_to_add, val in enumerate(y_index_to_expand):
            if val:
                world[idx].insert(idx_to_add+1+hit, '.')
                hit += 1
    return world


def find_galaxies(world):
    galaxies = []
    for x_idx, x in enumerate(world):
        for y_idx in find_indices(x, '#'):
            galaxies.append((x_idx, y_idx))
    return galaxies


def distance(a, b):
    return abs(b[0]-a[0]) + abs(b[1]-a[1])


def find_paths(galaxies):
    pairs_recorded = defaultdict(list)
    paths = []
    for a_idx, a_coords in enumerate(galaxies):
        for b_idx, b_coords in enumerate(galaxies):
            if a_idx == b_idx:
                continue
            if b_coords in pairs_recorded and a_coords in pairs_recorded[b_coords]:
                continue
            dist = distance(a_coords, b_coords)
            paths.append(dist)
            print(a_idx+1, a_coords, " -> ", b_idx+1, b_coords, " ", "Dist = ", dist)
            pairs_recorded[a_coords].append(b_coords)
    print(len(paths), ' paths recorded')
    return paths


def part1(input):
    world = [list(i) for i in input.split('\n')]
    world = galaxy_expansion(world)
    galaxies = find_galaxies(world)
    paths = find_paths(galaxies)
    return sum(paths)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
