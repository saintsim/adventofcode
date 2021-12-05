#!/usr/bin/env python3

from src.day08.part1 import parse, run_program
from copy import deepcopy


def accumulator(lines):
    program = parse(lines)
    for line_to_change in range(len(program)):
        new_program = change_line_x(deepcopy(program), line_to_change)
        if new_program:
            loop_type, total = run_program(new_program)
            if loop_type == 'finite':
                return total


def change_line_x(program, line_to_change):
    instruction = program[line_to_change]
    if instruction.operation in ['nop', 'jmp']:
        program[line_to_change].operation = 'nop' if instruction.operation == 'jmp' else 'jmp'
    else:
        return None
    return program


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(accumulator(lines)))
