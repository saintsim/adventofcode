#!/usr/bin/env python3

import part1


def sonar_sweep_part2(input):
    sums = []
    for idx, el in enumerate(input):
        sums.append(el + input[idx-1] + input[idx-2]) if idx > 1 else None
    return part1.sonar_sweep(sums)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(sonar_sweep_part2(list(map(int, file.readlines())))))
