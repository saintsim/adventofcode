#!/usr/bin/env python3

from collections import defaultdict
from part1 import parse


def subset(main_string, subset):
    return set(subset).issubset(set(main_string))


def determine_mapping(inputs):
    code_to_number = {}
    by_size = defaultdict(list)
    code_for_number = {}
    for input in inputs:
        input_str = ''.join(sorted(input))
        by_size[len(input)].append(input_str)
    code_to_number[by_size[2][0]] = 1
    code_for_number[1] = by_size[2][0]
    code_to_number[by_size[4][0]] = 4
    code_to_number[by_size[3][0]] = 7
    code_to_number[by_size[7][0]] = 8
    code_for_number[8] = by_size[7][0]
    for six_option in by_size[6]:
        if not subset(six_option, code_for_number[1]):
            code_to_number[six_option] = 6
        elif subset(six_option,by_size[4][0]):
            code_to_number[six_option] = 9
            code_for_number[9] = six_option
        else:
            code_to_number[six_option] = 0
    for five_option in by_size[5]:
        if subset(five_option, code_for_number[1]):
            code_to_number[five_option] = 3
        elif subset(five_option, set(code_for_number[8]) - set(code_for_number[9])):
            code_to_number[five_option] = 2
        else:
            code_to_number[five_option] = 5
    return code_to_number


def solve_segments(input):
    signals = parse(input)
    count = 0
    signal_map = {}
    for idx, inputs in enumerate(signals[0]):
        signal_map = determine_mapping(inputs)
        number_str = ''
        for output in signals[1][idx]:
            output_str = ''.join(sorted(output))
            number_str = number_str + str(signal_map[output_str])
        print(number_str)
        count += int(number_str)
    return count


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(solve_segments(lines)))