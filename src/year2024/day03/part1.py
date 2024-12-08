#!/usr/bin/env python3

import re
MUL_REGEX = r'mul\(([0-9]{1,3})\,([0-9]{1,3})\)'


def part1(input):
    total = 0
    input_list = list(input)
    for idx, letter in enumerate(input_list):
        if letter == 'm':
            trial_input = ''.join([('' if idx+x > len(input_list)-1 else input_list[idx+x]) for x in range(12)])
            is_mul = re.match(MUL_REGEX, trial_input)
            if is_mul is None:
                continue
            left, right = is_mul.groups()
            total += int(left) * int(right)
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
