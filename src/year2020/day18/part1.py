#!/usr/bin/env python3


def sum_expansion(lines):
    sums = [int(sum_compute(line)) for line in lines]
    return sum(sums)


def sum_compute(line):
    i = 0
    num_a, num_b, operator = '', '', ''
    while i < len(line):
        current_token = line[i]
        if current_token == '(':
            bracket_count = 1
            sum_to_recurse = ''
            i += 1
            while bracket_count != 0:
                current_token = line[i]
                if current_token == '(':
                    bracket_count += 1
                elif current_token == ')':
                    bracket_count -= 1
                sum_to_recurse += current_token
                i += 1
            current_token = sum_compute(sum_to_recurse[:-1])
        if str(current_token).isnumeric():
            if num_a == '':
                num_a = current_token
            elif num_b == '':
                num_b = current_token
            else:
                num_a = eval(num_a + operator + num_b)
                num_b = ''
                operator = ''
        elif current_token in ['*', '+']:
            if num_a != '' and num_b != '' and operator != '':
                num_a = eval(str(num_a) + operator + str(num_b))
                num_b = ''
            operator = current_token
        i += 1
    if num_a != '' and num_b != '' and operator != '':
        num_a = eval(str(num_a) + operator + str(num_b))
    return num_a


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(sum_expansion(lines)))
