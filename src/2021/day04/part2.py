#!/usr/bin/env python3

from part1 import parse, row_check, col_check, winning_score, NUMBERS_TO_CALL, CALLED, BOARDS, BOARD_SIZE

WINNERS = set()


def check_for_winners_2(called_number):
    print 'Called ' + called_number
    if len(CALLED) < BOARD_SIZE:
        return
    won = False
    for board_num, board in enumerate(BOARDS):
        for x, row in enumerate(board):
            if row_check(row):
                won = True
                break
            if col_check(board, x):
                won = True
                break
        if won:
            WINNERS.add(board_num)
            won = False
            if len(BOARDS) == len(WINNERS):
                return winning_score(board, called_number)


def play_game2():
    for called_number in NUMBERS_TO_CALL:
        CALLED.append(called_number)
        winner = check_for_winners_2(called_number)
        if winner:
            return winner


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        NUMBERS_TO_CALL, BOARDS = parse(lines)
        print('Result: ' + str(play_game2()))