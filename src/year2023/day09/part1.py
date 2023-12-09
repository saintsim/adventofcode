#!/usr/bin/env python3


def pt1_reverse_calc(all_diffs):
    all_diffs[0].append(all_diffs[0][-1])
    for idx, diff_line in enumerate(all_diffs):
        if idx == 0:
            continue
        all_diffs[idx].append(diff_line[-1] + all_diffs[idx - 1][-1])
    return all_diffs[-1][-1]


def calc_next_number(line, reverse_calc_func):
    diffs = [int(t) for t in line.split()]
    all_diffs = [diffs]
    while True:
        new_diff_list = []
        for idx in list(range(len(diffs)))[:-1]:
            new_diff_list.append(diffs[idx + 1] - diffs[idx])
        all_diffs.append(new_diff_list)
        diffs = new_diff_list
        if len(set(diffs)) == 1:  # all are the same value
            all_diffs.reverse()
            return reverse_calc_func(all_diffs)


def part1(input):
    return sum([calc_next_number(line, pt1_reverse_calc) for line in input.split("\n")])


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
