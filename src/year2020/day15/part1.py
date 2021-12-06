#!/usr/bin/env python3

from collections import Counter

SEEN_BEFORE = dict()
COUNT = Counter()


def number_spoken(sequence, iterations):
    for idx, val in enumerate(sequence):
        add_item(idx, val)
    prev = sequence[-1]
    for i in range(len(sequence), iterations):
        next = 0 if COUNT[prev] == 1 else SEEN_BEFORE[prev][1] - SEEN_BEFORE[prev][0]
        add_item(i, next)
        prev = next
    return prev


def add_item(idx, val):
    SEEN_BEFORE[val] = [SEEN_BEFORE[val][-1], idx] if COUNT[val] > 0 else [idx]
    COUNT[val] += 1


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = list(map(int, file.readline().split(',')))
        print('Result: ' + str(number_spoken(lines, 2020)))