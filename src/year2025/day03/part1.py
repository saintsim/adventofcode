#!/usr/bin/env python3

def part1(input):
    total = 0
    for line in input.split("\n"):
        batteries = list(map(int, line))
        b1_max = max(batteries[:-1])
        b1_loc = batteries.index(b1_max)
        b2_max = max(batteries[b1_loc + 1:])
        biggest = int(str(b1_max) + str(b2_max))
        print(biggest)
        total += biggest
    print("---")
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
