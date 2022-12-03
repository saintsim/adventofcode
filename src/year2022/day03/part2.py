#!/usr/bin/env python3


def rucksacks(input):
    total = 0
    line_count = 0
    last_three_lines = []
    for line in input:
        if line_count != 2:
            last_three_lines.append(set(line))
            line_count += 1
            continue
        in_all = last_three_lines[0].intersection(last_three_lines[1], set(line))
        score = 0
        for item in in_all:
            if item == '\n':
                continue
            if item == item.lower():
                score = (ord(item)-ord('a'))+1
            else:
                score = (ord(item) - ord('A')) + 27
        print(score)
        total += score
        line_count = 0
        last_three_lines = []
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(rucksacks(file.readlines())))
