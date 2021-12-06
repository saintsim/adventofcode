#!/usr/bin/env python3

from part1 import parse, draw_grid


if __name__ == '__main__':
    with open('input', 'r') as file:
        max_x, max_y, lines = parse(file.readlines())
        print('Result: ' + str(draw_grid(max_x, max_y, lines, True)))
