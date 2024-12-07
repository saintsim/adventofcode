#!/usr/bin/env python3

from libraries.parsing.matrix import parse_matrix

MATRIX = []
XMAS_COORDS = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)],

]


def matrix_letter(new_coord):
    if new_coord[0] >= len(MATRIX[0]) or new_coord[0] < 0 or new_coord[1] >= len(MATRIX) or new_coord[1] < 0:
        return 'X'
    return MATRIX[new_coord[0]][new_coord[1]]


def contains_xmas(root):
    for coords in XMAS_COORDS:
        letters = []
        for coord in coords:
            new_coord = (root[0] + coord[0], root[1] + coord[1])
            letters.append(matrix_letter(new_coord))
        letters.sort()
        if letters != ['M', 'S']:
            return False
    return True


def part2(input):
    count = 0
    global MATRIX
    MATRIX = parse_matrix(input)
    for y, row in enumerate(MATRIX):
        for x, cell in enumerate(row):
            if cell == 'A':
                if contains_xmas((y, x)):
                    count += 1
    return count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
