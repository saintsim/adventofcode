#!/usr/bin/env python3


def rucksacks(input):
    total = 0
    for line in input:
        section1 = set(line[:len(line)//2])
        section2 = set(line[len(line)//2:])
        in_both = section1.intersection(section2)
        for item in in_both:
            if item == item.lower():
                total += (ord(item)-ord('a'))+1
            else:
                total += (ord(item) - ord('A')) + 27
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(rucksacks(file.readlines())))
