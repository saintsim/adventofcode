#!/usr/bin/env python3


def sonar_sweep(input):
    return sum(idx != 0 and el-input[idx-1] > 0 for idx, el in enumerate(input))


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(sonar_sweep(list(map(int, file.readlines())))))
