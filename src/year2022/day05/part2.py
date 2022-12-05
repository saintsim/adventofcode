#!/usr/bin/env python3

import re
from part1 import MOVES, STACKS, run_moves, parse


def run_moves_part2():
    for move in MOVES:
        items = []
        for _ in range(move.number_to_move):
            items.append(STACKS[move.stack_from-1].pop())
        items.reverse()
        for item in items:
            STACKS[move.stack_to-1].append(item)


def stacks(input):
    parse(input)
    run_moves_part2()
    result = ''
    for stack in STACKS:
        result += stack[-1]
    return result


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(stacks(file.readlines())))

