#!/usr/bin/env python3

MATRIX = []


def parse(input):
    for line in input.split('\n'):
        MATRIX.append(list(line))


def is_on_grid(node):
    if node[0] < 0 or node[0] > len(MATRIX) - 1:
        print('skip: ' + str(node))
        return False
    if node[1] < 0 or node[1] > len(MATRIX[0]) - 1:
        print('skip: ' + str(node))
        return False
    return True


def find_antinodes(by_type):
    nodes = set()
    for key, vals in by_type.items():
        for idx_1, ant1 in enumerate(vals):
            for idx_2, ant2 in enumerate(vals):
                if idx_1 == idx_2:
                    continue
                antinode = (ant1[0] - (ant2[0] - ant1[0]), ant1[1] - (ant2[1] - ant1[1]))
                if is_on_grid(antinode):
                    nodes.add(antinode)
    print(nodes)
    return len(nodes)


def part1(input):
    parse(input)
    by_type = {}
    for y, row in enumerate(MATRIX):
        for x, cell in enumerate(row):
            if cell != '.':
                by_type.setdefault(cell, []).append((y, x))
    return find_antinodes(by_type)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
