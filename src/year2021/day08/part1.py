#!/usr/bin/env python3

def parse(input):
    inputs = []
    outputs = []
    for line in input:
        line_inputs, line_outputs = line.split(" | ")
        inputs.append((line_inputs.split()))
        outputs.append((line_outputs.split()))
    return [inputs, outputs]


def solve_segments(input):
    signals = parse(input)
    count = 0
    for outputs in signals[1]:
        for output in outputs:
            if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
                count += 1
    return count


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(solve_segments(lines)))