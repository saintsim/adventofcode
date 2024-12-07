#!/usr/bin/env python3

from libraries.parsing.matrix import parse_matrix

MATRIX = []
COORDS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),

    (0, -1),
    (0, 1),

    (1, -1),
    (1, 0),
    (1, 1)
]


def matrix_letter_found(new_coord, letter):
    if new_coord[0] >= len(MATRIX[0]) or new_coord[0] < 0 or new_coord[1] >= len(MATRIX) or new_coord[1] < 0:
        return False
    if MATRIX[new_coord[0]][new_coord[1]] == letter:
        return True
    return False


def contains_xmas(root):
    count = 0
    for coord in COORDS:
        path = [root]
        new_coord = root
        found = True
        for letter in ['M', 'A', 'S']:
            new_coord = (new_coord[0] + coord[0], new_coord[1] + coord[1])
            found_coord = matrix_letter_found(new_coord, letter)
            path.append(new_coord)
            if not found_coord:
                found = False
                break
        if found:
            print(path)
            count += 1
    return count


def part1(input):
    count = 0
    global MATRIX
    MATRIX = parse_matrix(input)
    for y, row in enumerate(MATRIX):
        for x, cell in enumerate(row):
            if cell == 'X':
                count += contains_xmas((y, x))
    return count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
