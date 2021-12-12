#!/usr/bin/env python3

from collections import Counter
from part1 import parse

GRAPH = {}
PATHS = []


def small_cave_limit_reached(path, node_to_add):
    if node_to_add.islower() and node_to_add in path:
        for key, val in Counter(path).items():
            if key.islower() and val > 1:
                return True
    return False


def cave_path_finder(current_node, current_path):
    current_path.append(current_node)
    if current_node == "end":
        if current_path not in PATHS:
            print(current_path)
            PATHS.append(current_path)
    else:
        for next_node in GRAPH[current_node]:
            if next_node != "end" and small_cave_limit_reached(current_path, next_node):
                continue
            next_path = list(current_path)
            cave_path_finder(next_node, next_path)


def cave_paths(input):
    parse(input)
    cave_path_finder("start", [])
    return len(PATHS)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(cave_paths(lines)))
