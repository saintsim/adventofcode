#!/usr/bin/env python3

MATRIX = []


def parse(input):
    for line in input.split('\n'):
        MATRIX.append(list(line))


def find_antinodes(by_type):
    for key, val in by_type.items():
        pass


def part1(input):
    parse(input)
    by_type = {}
    for y, row in enumerate(MATRIX):
        for x, cell in enumerate(row):
            if cell != '.':
                by_type.setdefault(cell,[]).append((y,x))
                # locate anti-nodes
                #by_type[(y,x), cell)
    find_antinodes(by_type)
    pass


if __name__ == '__main__':
    with open('example', 'r') as file:
        print('Result: ' + str(part1(file.read())))
