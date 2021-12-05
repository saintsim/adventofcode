#!/usr/bin/env python3

import collections


def filter_entries(entries, i, bit_to_use):
    to_keep = []
    for entry in entries:
        if int(entry[i]) == bit_to_use:
            to_keep.append(entry)
    return to_keep


def flip_bit(bit):
    return 1 if bit == 0 else 0


def get_rating(lines, is_co2):
    entries = lines
    for i in xrange(len(lines[0])):
        col = []
        for row in entries:
            col.append(int(row[i]))
        most_common = collections.Counter(col).most_common()
        if int(most_common[0][1]) == int(most_common[1][1]):
            bit_to_use = 1
        else:
            bit_to_use = int(most_common[0][0])
        bit_to_use = flip_bit(bit_to_use) if is_co2 else bit_to_use
        entries = filter_entries(entries, i, bit_to_use)
        if len(entries) == 1:
            return int(''.join([str(a) for a in entries[0]]), 2)


def find_solution(lines):
    oxygen_rating = get_rating(lines, False)
    co2_rating = get_rating(lines, True)
    return oxygen_rating * co2_rating


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(find_solution(lines)))
