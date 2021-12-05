#!/usr/bin/env python3

import re


class Instruction:
    def __init__(self, operation, value):
        # operation (acc, jmp, or nop)
        # argument (a signed number like +4 or -20)
        self.operation = operation
        self.value = int(value)

    def __str__(self):
        return self.operation + ' ' + self.value


def accumulator(lines):
    _, total = run_program(parse(lines))
    return total


def run_program(program):
    total, i, lines_visited = 0, 0, set()
    while i < len(program):
        if i in lines_visited:
            return 'infinite', total
        lines_visited.add(i)
        op, val = program[i].operation, program[i].value
        if op == 'acc':
            total += val
        elif op == 'jmp':
            i += val
            continue
        i += 1
    return 'finite', total


def parse(lines):
    return [Instruction(*line.split()) for line in lines]


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(accumulator(lines)))
