#!/usr/bin/env python3

from part1 import score


def rucksacks(input):
    total = 0
    for i in range(0, len(input), 3):
        in_all = set(input[i]).intersection(set(input[i+1]), set(input[i+2]))
        total += score(next(iter(in_all)))
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(rucksacks(lines)))
