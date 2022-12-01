#!/usr/bin/env python3


def calories(input):
    elf_calories = 0
    max_calories = 0
    for line in input:
        if line == '\n':
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line)
    return max_calories


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(calories(file.readlines())))
