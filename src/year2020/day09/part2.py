#!/usr/bin/env python3


def encryption_weakness(lines, target):
    for start in range(0, len(lines)):
        for end in range(start+1, len(lines)):
            current_sum = sum(lines[start:end])
            if current_sum == target:
                return min(lines[start:end]) + max(lines[start:end])
            if current_sum > target:
                break


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [int(line.strip()) for line in file.readlines()]
        # for sample
        # print('Result: ' + str(encryption_weakness(lines, 127)))
        print('Result: ' + str(encryption_weakness(lines, 21806024)))
