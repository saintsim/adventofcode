#!/usr/bin/env python3


def score(item):
    return (ord(item)-ord('a')) + 1 if (item == item.lower()) else (ord(item) - ord('A')) + 27


def rucksacks(input):
    total = 0
    for line in input:
        mid = len(line)//2
        in_both = set(line[:mid]) & set(line[mid:])
        total += score(next(iter(in_both)))
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(rucksacks(file.readlines())))
