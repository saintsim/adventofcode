#!/usr/bin/env python3

from part1 import compute_range


def overlap_atall(bucket1, bucket2):
    return len(set(bucket1) & set(bucket2)) > 0


def camp(input):
    overlaps = 0
    for line in input:
        elves_ranges = []
        for elf in line.split(','):
            elves_ranges.append(elf.split('-'))
        bucket1 = compute_range(elves_ranges[0][0], elves_ranges[0][1])
        bucket2 = compute_range(elves_ranges[1][0], elves_ranges[1][1])
        overlaps += overlap_atall(bucket1, bucket2)
    print(overlaps)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(camp(lines)))

