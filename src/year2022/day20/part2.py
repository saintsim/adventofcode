#!/usr/bin/env python3

from part1 import grove

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(grove(lines, 10, 811589153)))
