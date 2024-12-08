#!/usr/bin/env python3

MATRIX = []


def parse(input):
    for line in input.split('\n'):
        MATRIX.append(list(line))


def is_on_grid(node):
    if node[0] < 0 or node[0] > len(MATRIX)-1:
        print('skip: ' + str(node))
        return False
    if node[1] < 0 or node[1] > len(MATRIX[0])-1:
        print('skip: ' + str(node))
        return False
    return True


def find_antinodes(by_type):
    nodes = set()
    for key, vals in by_type.items():
        for idx_1, val_1 in enumerate(vals):
            for idx_2, val_2 in enumerate(vals):
                if idx_1 == idx_2:
                    continue
                y_diff = val_2[0] - val_1[0]
                x_diff = val_2[1] - val_1[1]
                antinode_1 = val_1
                antinode_2 = val_2
                while True:
                    antinode_1 = (antinode_1[0] - y_diff, antinode_1[1] - x_diff)
                    if is_on_grid(antinode_1):
                        nodes.add(antinode_1)
                    else:
                        break
                while True:
                    antinode_2 = (antinode_2[0] + y_diff, antinode_2[1] + x_diff)
                    if is_on_grid(antinode_2):
                        nodes.add(antinode_2)
                    else:
                        break
                # add the antennas
                nodes.add(val_1)
                nodes.add(val_2)
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
