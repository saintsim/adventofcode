#!/usr/bin/env python3

import re


def parse(input):
    patterns_input, towels_input = input.split('\n\n')
    patterns = [x.strip() for x in patterns_input.split(',')]
    towels = towels_input.split('\n')
    return patterns, towels


def is_valid(towel, patterns):
    if towel == '':
        return True
    valid = False
    for pattern in patterns:
        if towel.startswith(pattern):
            tokens_left = re.sub(pattern, '', towel, 1)
            if tokens_left == '':
                return True
            valid = is_valid(tokens_left, patterns)
            if valid:
                return True
    return valid


def part1(input):
    total = 0
    patterns, towels = parse(input)
    for towel in towels:
        if is_valid(towel, patterns):
            total += 1
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
