#!/usr/bin/env python3

def part1(input):
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
    for j in list1:
        total = total + abs(list1[i]-list2[i])
        i = i+1
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))