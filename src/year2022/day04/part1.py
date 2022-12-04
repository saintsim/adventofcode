#!/usr/bin/env python3

def compute_range(elf_from, elf_to):
    return list(range(int(elf_from), int(elf_to) + 1))


def overlap(bucket1, bucket2):
    return set(bucket1).issubset(set(bucket2)) or set(bucket2).issubset(set(bucket1))


def camp(input):
    overlaps = 0
    for line in input:
        elves_ranges = []
        for elf in line.split(','):
            elves_ranges.append(elf.split('-'))
        bucket1 = compute_range(elves_ranges[0][0], elves_ranges[0][1])
        bucket2 = compute_range(elves_ranges[1][0], elves_ranges[1][1])
        overlaps += overlap(bucket1, bucket2)
    return overlaps


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(camp(lines)))

