#!/usr/bin/env python3

NUMBERS_TO_CALL = []
CALLED = []
BOARDS = []
BOARD_SIZE = 5


def parse(lines):
    board_number = -1
    board = []
    numbers_to_call = []
    boards = []
    for i, line in enumerate(lines):
        if i == 0:
            numbers_to_call = lines[i].split(",")
            continue
        if line == '\n':
            board_number += 1
            if board:
                boards.append(board)
                board = []
            continue
        board.append(line.split())
    if board:
        boards.append(board)
    return numbers_to_call, boards


def check_for_winners(called_number):
    print 'Called ' + called_number
    if len(CALLED) < BOARD_SIZE:
        return
    for board in BOARDS:
        for x, row in enumerate(board):
            if row_check(row):
                return winning_score(board, called_number)
            if col_check(board, x):
                return winning_score(board, called_number)


def row_check(row):
    for num in row:
        if num not in CALLED:
            return False
    return True


def col_check(board, x):
    for row in board:
        if row[x] not in CALLED:
            return False
    return True


def winning_score(board, called_number):
    sum = 0
    for row in board:
        for cell in row:
            if cell not in CALLED:
                sum += int(cell)
    return int(called_number) * sum


def play_game():
    for called_number in NUMBERS_TO_CALL:
        CALLED.append(called_number)
        winner = check_for_winners(called_number)
        if winner:
            return winner


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        NUMBERS_TO_CALL, BOARDS = parse(lines)
        print('Result: ' + str(play_game()))