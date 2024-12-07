#!/usr/bin/env python3


def calc(total, inputs, expected_total):
    run_result = False
    for idx, input in enumerate(inputs):
        if idx == len(inputs) - 1:
            run_result = True
            break
        plus_total = total + inputs[idx+1]
        if plus_total <= expected_total:
            plus_total = calc(plus_total, inputs[idx+1:], expected_total)
            if plus_total == expected_total:
                return plus_total
        multi_total = total * inputs[idx + 1]
        if multi_total <= expected_total:
            multi_total = calc(multi_total, inputs[idx+1:], expected_total)
            if multi_total == expected_total:
                return multi_total
    if run_result:
        if total == expected_total:
            return expected_total
    return 0


def part1(input):
    total = 0
    for line in input.split('\n'):
        expected_total, components = line.split(': ')
        components = list(map(int, components.split()))
        sum = calc(components[0], components, int(expected_total))
        total += sum
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))