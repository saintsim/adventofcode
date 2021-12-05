#!/usr/bin/env python3

import collections


def find_solution(lines):
    bit_array = []
    for i in xrange(len(lines[0])):
        bit_array.append([])
    for line in lines:
        for i, cell in enumerate(line):
            bit_array[i].append(int(cell))
    gamma_bin = epsilon_bin = ''
    for bit in bit_array:
        gamma_bin += str(collections.Counter(bit).most_common()[0][0])
    for bit in gamma_bin:
        epsilon_bin += "0" if bit == "1" else "1"
    gamma_rate = int(gamma_bin, 2)
    epsilon_rate = int(epsilon_bin, 2)
    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(find_solution(lines)))
