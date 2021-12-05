#!/usr/bin/env python3

import re

COMBINATIONS = list()


def bit_mask(lines):
    i, memory = 0, dict()
    while i < len(lines):
        mask = re.match('mask = ([X10]+)', lines[i]).groups()[0]
        i += 1
        while i < len(lines) and 'mem' in lines[i]:
            index, value = re.match(r'mem\[(\d+)\] = (\d+)$', lines[i]).groups()
            index_bin = "{:0>36b}".format(int(index))
            result_bin = ''
            for idx, value_bit in enumerate(index_bin):
                if mask[idx] == '0':
                    result_bin += str(value_bit)
                elif mask[idx] == '1':
                    result_bin += '1'
                else:  # X
                    result_bin += 'F'
            if 'F' in result_bin:
                calc_combinations(list(result_bin))
                global COMBINATIONS
                result_bin_combinations = COMBINATIONS
                COMBINATIONS = list()
            else:
                result_bin_combinations = [result_bin]
            for result_bin in result_bin_combinations:
                memory[int(result_bin, 2)] = int(value)
            i += 1
    return sum(memory.values())


def calc_combinations(bin_line):
    floating_indexes = [i for i, x in enumerate(bin_line) if x == 'F']
    if len(floating_indexes) == 0:
        COMBINATIONS.append("".join(bin_line))
    for bin_val in ['0', '1']:
        bin_line[floating_indexes[0]] = bin_val
        calc_combinations(list(bin_line))


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(bit_mask(lines)))
