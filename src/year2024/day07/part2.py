#!/usr/bin/env python3

def calc_part2(total, inputs, expected_total, ops):
    if len(inputs) > 1:
        for op in ['+', '*', '||']:
            op_total = 0
            match op:
                case '+':
                    op_total = total + inputs[1]
                case '||':
                    op_total = int(str(total)+str(inputs[1]))
                case '*':
                    op_total = total * inputs[1]
            if op_total <= expected_total:
                op_total = calc_part2(op_total, inputs[1:], expected_total, ops+[op])
                if op_total == expected_total:
                    return op_total
    else:
        if total == expected_total:
            return expected_total
    return 0


def part2(input):
    total = 0
    for line in input.split('\n'):
        expected_total, components = line.split(': ')
        components = list(map(int, components.split()))
        sum = calc_part2(components[0], components, int(expected_total), [])
        # if sum != 0:
        #    print((' [Invalid]' if sum == 0 else ' [Valid]') + ',' + line)
        #if sum == 0:
        #    print(line)
        total += sum
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))