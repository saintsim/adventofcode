#!/usr/bin/env python3

import re

STACKS = [[], [], [], [], [], [], [], [], []]
MOVES = []


class Move:
    def __init__(self, number_to_move, stack_from, stack_to):
        self.number_to_move = int(number_to_move)
        self.stack_from = int(stack_from)
        self.stack_to = int(stack_to)


def parse(input):
    global STACKS
    max_stack = 0
    for line in input:
        # cols = 1, 5, 9
        if '[' in line or ']' in line:
            stack_number = 0
            stack_position_idx = 1
            while True:
                if stack_position_idx >= len(line):
                    break
                if line[stack_position_idx].isalpha():
                    STACKS[stack_number].append(line[stack_position_idx])
                stack_number += 1
                stack_position_idx += 4
            max_stack = stack_number if stack_number > max_stack else max_stack
        elif 'move' in line:
            number_to_move, stack_from, stack_to = re.match(r'move ([\d]+) from (\d) to (\d)[\n]*', line).groups()
            MOVES.append(Move(number_to_move, stack_from, stack_to))
    STACKS = STACKS[:max_stack]
    for stack in STACKS:
        stack.reverse()
    print(STACKS)


def run_moves():
    for move in MOVES:
        for _ in range(move.number_to_move):
            item = STACKS[move.stack_from-1].pop()
            STACKS[move.stack_to-1].append(item)


def stacks(input):
    parse(input)
    run_moves()
    print('---')
    result = ''
    for stack in STACKS:
        result += stack[-1]
    print(STACKS)
    print('---')
    return result


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(stacks(file.readlines())))

