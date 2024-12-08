#!/usr/bin/env python3

import re
MUL_REGEX = r'mul\(([0-9]{1,3})\,([0-9]{1,3})\)'
DO_OR_DONT_REGEX = r'(do\(\))|(don\'t\(\))'
DO = 1
DONT = 0
SKIP = None


def part2(input):
    total = 0
    input_list = list(input)
    enabled = True
    for idx, letter in enumerate(input_list):
        if letter == 'd':
            trial_input = ''.join([('' if idx + x > len(input_list) - 1 else input_list[idx + x]) for x in range(7)])
            res = do_or_dont(trial_input)
            if res == DO or res == DONT:
                enabled = res
            continue
        if enabled and letter == 'm':
            trial_input = ''.join([('' if idx+x > len(input_list)-1 else input_list[idx+x]) for x in range(12)])
            is_mul = re.match(MUL_REGEX, trial_input)
            if is_mul is None:
                continue
            left, right = is_mul.groups()
            total += int(left) * int(right)
    return total


def do_or_dont(input):
    matches = re.match(DO_OR_DONT_REGEX, input)
    if matches is None:
        return SKIP
    do, dont = matches.groups()
    return DONT if do is None else DO


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
