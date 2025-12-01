#!/usr/bin/env python3

def part2(input):
    current = 50
    zero_counter = 0
    for line in input.split('\n'):
        direction = line[0]
        amount = int(line[1:])
        current, zero_counter_change = scarps_mod(direction, current, amount)
        zero_counter += zero_counter_change
    return zero_counter


def scarps_mod(direction, current, amount):
    zero_counter = 0
    for i in range(amount):
        if direction == 'L':
            next_number = (current - 1) % 100
        else:
            next_number = (current + 1) % 100
        if next_number == 0:
            zero_counter += 1
        current = next_number
    return current, zero_counter


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
