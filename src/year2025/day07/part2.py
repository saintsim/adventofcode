#!/usr/bin/env python3

from collections import defaultdict

PATH_LOCATION_MAP = dict()


def new_beam_location(point):
    if point in PATH_LOCATION_MAP:
        return PATH_LOCATION_MAP[point]
    else:
        loc = point[0] + 1, point[1]
        PATH_LOCATION_MAP[point] = loc
        return loc


def part2(input):
    world = [list(line) for line in input.split('\n')]
    # we know S is on the first line
    s_location = (0, world[0].index('S'))
    paths = defaultdict(int)
    paths[new_beam_location(s_location)] = 1
    line_num = 0
    for line in world[2:]:
        print(line_num)
        line_num += 1
        global PATH_LOCATION_MAP
        PATH_LOCATION_MAP = dict()
        new_paths = defaultdict(int)
        if '^' in line:
            for path, val in paths.items():
                next_beam_location = new_beam_location(path)
                if line[next_beam_location[1]] == '.':
                    new_paths[next_beam_location] += val
                else:
                    new_paths[(next_beam_location[0], next_beam_location[1]-1)] += val
                    new_paths[(next_beam_location[0], next_beam_location[1]+1)] += val
        else:
            for path, val in paths.items():
                new_paths[new_beam_location(path)] += val
        # print(new_paths)
        paths = new_paths
    return sum(paths.values())


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
