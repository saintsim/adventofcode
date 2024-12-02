#!/usr/bin/env python3

SAFE = 1
UNSAFE = 0


def safe_check(tokens):
    if tokens[1] > tokens[0]:
        # increasing
        for idx, line in enumerate(range(len(tokens) - 1)):
            if tokens[idx+1] > tokens[idx]:
                diff = tokens[idx+1] - tokens[idx]
                if diff < 1 or diff > 3:
                    return UNSAFE
            else:
                return UNSAFE
        return SAFE
    else:
        # decreasing
        for idx, line in enumerate(range(len(tokens)-1)):
            if tokens[idx] > tokens[idx+1]:
                diff = tokens[idx] - tokens[idx+1]
                if diff < 1 or diff > 3:
                    return UNSAFE
            else:
                return UNSAFE
        return SAFE
    pass


def part1(input):
    safe_count = 0
    for line in input.split('\n'):
        if safe_check(list(map(int, line.split()))) == SAFE:
            safe_count += 1
    return safe_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))