#!/usr/bin/env python3

from src.day19.part1 import rule_checker

if __name__ == '__main__':
    with open('input2', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        # add a max recursion depth of 100 (longest message is just under 100 is the rationale)
        print('Result: ' + str(rule_checker(lines, 100)))
