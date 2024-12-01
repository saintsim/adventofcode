#!/usr/bin/env python3

from collections import Counter


def part2(input):
    list1 = []
    list2 = []
    for line in input.split('\n'):
        left, right = line.split()
        list1.append(int(left))
        list2.append(int(right))
    list1.sort()
    list2.sort()
    i = 0
    total = 0
    right_counter = Counter(list2)
    for _ in list1:
        total += (list1[i] * right_counter[list1[i]])
        i = i+1
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))