#!/usr/bin/env python3

GRAPH = {}
PATHS = []


def add_to_graph(from_cave, to_cave):
    if from_cave not in GRAPH:
        GRAPH[from_cave] = []
    if to_cave != "start":
        GRAPH[from_cave].append(to_cave)


def parse(input):
    for line in input:
        from_cave, to_cave = line.split("-")
        # add both directions
        add_to_graph(from_cave, to_cave)
        add_to_graph(to_cave, from_cave)
    return GRAPH


def cave_path_finder(current_node, current_path):
    current_path.append(current_node)
    if current_node == "end":
        if current_path not in PATHS:
            print(current_path)
            PATHS.append(current_path)
    else:
        for next_node in GRAPH[current_node]:
            if next_node.islower() and next_node != "end" and next_node in current_path:
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
