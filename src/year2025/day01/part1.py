#!/usr/bin/env python3

def part1(input):
    current = 50
    zero_counter = 0
    for line in input.split('\n'):
        direction = line[0]
        amount = int(line[1:])
        if direction == 'L':
            current = (current - amount) % 100
        elif direction == 'R':
            current = (current + amount) % 100
        else:
            raise "Something wrong"
        print(line, ": ", direction, " ", amount, " ", current)
        if current == 0:
            zero_counter += 1
    return zero_counter


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
