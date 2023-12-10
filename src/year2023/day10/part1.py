#!/usr/bin/env python3


class Node:

    def __init__(self, next_coord, next_direction):
        self.visited = set()
        self.next_coord = next_coord
        self.next_direction = next_direction
        self.done = False



DIR = {
    # go up
    'UP': (-1, 0),
    # go down
    'DOWN': (1, 0),
    # go left
    'LEFT': (0, -1),
    # go right
    'RIGHT': (0, 1)
}

GRAPH = []
ALL_VISITED = set()


def parse(input):
    return [list(line) for line in input]


def find_start_coord(maze):
    for idx, line in enumerate(maze):
        if 'S' in line:
            return (idx, line.index('S'))


def get_cell_value(maze, coord):
    if coord[0] < 0 or coord[1] < 0 or coord[0] > len(maze) or coord[1] > len(maze[0]):
        return None
    return maze[coord[0]][coord[1]]


def navigate_path(maze, node):
    next_coord = (node.next_coord[0] + node.next_direction[0], node.next_coord[1] + node.next_direction[1])
    if next_coord in ALL_VISITED:
        node.done = True
        return node
    else:
        ALL_VISITED.add(next_coord)
    if next_coord in node.visited:
        node.done = True
        return node
    node.next_coord = next_coord
    node.visited.add(next_coord)
    cell_value = get_cell_value(maze, next_coord)
    if cell_value is None or cell_value == '.':
        node.done = True
        return node
    if cell_value == '-' or cell_value == '|':
        return node
    if cell_value == 'L':
        if node.next_direction == DIR["DOWN"]:
            node.next_direction = DIR["RIGHT"]
        else:
            node.next_direction = DIR["UP"]
    elif cell_value == 'J':
        if node.next_direction == DIR["DOWN"]:
            node.next_direction = DIR["LEFT"]
        else:
            node.next_direction = DIR["UP"]
    elif cell_value == '7':
        if node.next_direction == DIR["RIGHT"]:
            node.next_direction = DIR["DOWN"]
        else:
            node.next_direction = DIR["LEFT"]
    elif cell_value == 'F':
        if node.next_direction == DIR["UP"]:
            node.next_direction = DIR["RIGHT"]
        else:
            node.next_direction = DIR["DOWN"]
    return node


def find_longest_path(maze, start_coord):
    all_done = []
    for label, direction in DIR.items():
        GRAPH.append(Node(start_coord, direction))
        all_done.append(False)

    while not all(all_done):
        for idx, node in enumerate(GRAPH):
            if node.done:
                continue
            navigate_path(maze, node)
            if node.done:
                all_done[idx] = True
    return max([len(g.visited) for g in GRAPH])


def part1(input):
    maze = parse(input)
    start_coord = find_start_coord(maze)
    return find_longest_path(maze, start_coord)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(part1(lines))
