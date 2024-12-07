#!/usr/bin/env python3


def calc(total, inputs, expected_total):
    if len(inputs) > 1:
        for op in ['+', '*']:
            op_total = 0
            match op:
                case '+':
                    op_total = total + inputs[1]
                case '*':
                    op_total = total * inputs[1]
            if op_total <= expected_total:
                op_total = calc(op_total, inputs[1:], expected_total)
                if op_total == expected_total:
                    return op_total
    else:
        if total == expected_total:
            return expected_total
    return 0


def part1(input):
    total = 0
    for line in input.split('\n'):
        expected_total, components = line.split(': ')
        components = list(map(int, components.split()))
        total += calc(components[0], components, int(expected_total))
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))