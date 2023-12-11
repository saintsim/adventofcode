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
    # cols (y)
    y_to_expand = []
    for idx, val in enumerate(y_index_to_expand):
        if val:
            y_to_expand.append(idx)
    return x_index_to_expand, y_to_expand


def adjust_galaxies_in_bigger_world(world, galaxies, adj_multiplier):
    x_index_to_expand, y_index_to_expand = galaxy_expansion(world)
    new_galaxies = []
    for galaxy in galaxies:
        x, y = galaxy[0], galaxy[1]
        x += get_adjustment(adj_multiplier, x, x_index_to_expand)
        y += get_adjustment(adj_multiplier, y, y_index_to_expand)
        new_galaxies.append((x, y))
    return new_galaxies


def get_adjustment(adj_multiplier, x, x_index_to_expand):
    x_adjust = 0
    if x > 0:
        for i, x_idx in enumerate(x_index_to_expand):
            if x_idx > x:
                break
            x_adjust += (adj_multiplier-1)
    return x_adjust


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


def part2(input):
    world = [list(i) for i in input.split('\n')]
    galaxies = find_galaxies(world)
    galaxies = adjust_galaxies_in_bigger_world(world, galaxies, 1000000)
    paths = find_paths(galaxies)
    return sum(paths)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
