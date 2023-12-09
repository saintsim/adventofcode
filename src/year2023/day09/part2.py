#!/usr/bin/env python3

from part1 import calc_next_number


def pt2_reverse_calc(all_diffs):
    all_diffs[0].append(all_diffs[0][-1])
    for idx, diff_line in enumerate(all_diffs):
        if idx == 0:
            continue
        all_diffs[idx].insert(0, diff_line[0] - all_diffs[idx-1][0])
    return all_diffs[-1][0]


def part2(input):
    return sum([calc_next_number(line, pt2_reverse_calc) for line in input.split("\n")])


if __name__ == '__main__':
    with open('input', 'r') as file:
         print('Result: ' + str(part2(file.read())))