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
                y_diff = ant2[0] - ant1[0]
                x_diff = ant2[1] - ant1[1]
                antinode = ant1
                while True:
                    antinode = (antinode[0] - y_diff, antinode[1] - x_diff)
                    if is_on_grid(antinode):
                        nodes.add(antinode)
                    else:
                        break
                # add the antennas
                nodes.add(ant1)
    print(nodes)
    return len(nodes)


def part2(input):
    parse(input)
    by_type = {}
    for y, row in enumerate(MATRIX):
        for x, cell in enumerate(row):
            if cell != '.':
                by_type.setdefault(cell, []).append((y, x))
    return find_antinodes(by_type)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
