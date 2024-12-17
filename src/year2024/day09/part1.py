#!/usr/bin/env python3

def parse(input):
    disk = []
    idx = 0
    for i in range(0, len(input), 2):
        for _ in range(int(input[i])):
            disk.append(str(idx))
        if i < len(input)-1:
            for _ in range(int(input[i+1])):
                disk.append('.')
        idx += 1
    return disk


def move_blocks(disk):
    idx = 0
    while True:
        if '.' not in disk or set(disk[idx:]) == {'.'}:
            return disk
        if disk[idx] == '.':
            item_to_move = None
            for back_element in range(len(disk)-1, -1, -1):
                if disk[back_element] != '.':
                    item_to_move = disk.pop(back_element)
                    break
            if item_to_move is not None:
                disk[idx] = item_to_move
        idx += 1


def calc_checksum(disk):
    total = 0
    for idx, element in enumerate(disk):
        if element != '.':
            total += int(element) * idx
    return total


def part1(input):
    disk = parse(input)
    disk = move_blocks(disk)
    return calc_checksum(disk)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
