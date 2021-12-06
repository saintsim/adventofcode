#!/usr/bin/env python3

import re


def bit_mask(lines):
    i, memory = 0, dict()
    while i < len(lines):
        mask = re.match('mask = ([X10]+)', lines[i]).groups()[0]
        i += 1
        while i < len(lines) and 'mem' in lines[i]:
            index, value = re.match(r'mem\[(\d+)\] = (\d+)$', lines[i]).groups()
            value_bin = "{:0>36b}".format(int(value))
            result_bin = ''
            for idx, value_bit in enumerate(value_bin):
                result_bin += value_bit if mask[idx] == 'X' else mask[idx]
            memory[index] = int(result_bin, 2)
            i += 1
    return sum(memory.values())


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(bit_mask(lines)))
