#!/usr/bin/env python3


def calories(input):
    elf_calories = 0
    calories_by_elf = []
    for line in input:
        if line == '\n':
            calories_by_elf.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
    calories_by_elf = sorted(calories_by_elf)
    return sum(calories_by_elf[-3:])


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(calories(file.readlines())))
