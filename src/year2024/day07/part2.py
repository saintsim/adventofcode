#!/usr/bin/env python3

def calc_part2(total, inputs, expected_total, ops):
    if len(inputs) > 1:
        plus_total = total + inputs[1]
        if plus_total <= expected_total:
            plus_total = calc_part2(plus_total, inputs[1:], expected_total, ops+['+'])
            if plus_total == expected_total:
                return plus_total
        concat_total = int(str(total)+str(inputs[1]))
        if concat_total <= expected_total:
            concat_total = calc_part2(concat_total, inputs[1:], expected_total, ops+['||'])
            if concat_total == expected_total:
                return concat_total
        multi_total = total * inputs[1]
        if multi_total <= expected_total:
            multi_total = calc_part2(multi_total, inputs[1:], expected_total, ops+['*'])
            if multi_total == expected_total:
                return multi_total
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