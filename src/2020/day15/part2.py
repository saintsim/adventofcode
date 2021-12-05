#!/usr/bin/env python3

from src.day15.part1 import number_spoken


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(number_spoken(lines, 30000000)))