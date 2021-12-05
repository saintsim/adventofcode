#!/usr/bin/env python3

import math


def get_highest_seat_id(lines):
    highest_seat_id = 0
    for line in lines:
        seat_id = get_seat_id(line)
        highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id
    return highest_seat_id


def get_seat_id(seat):
    seat_row = get_row_col_id(seat[:7], 0, 127)
    seat_col = get_row_col_id(seat[7:], 0, 7)
    seat_id = seat_row * 8 + seat_col
    return seat_id


def get_row_col_id(seat, lower, upper):
    if seat[0] in ['F', 'L']:
        # lower (F/L)
        if len(seat) == 1:
            return lower
        return get_row_col_id(seat[1:], lower, lower + int(math.floor((upper-lower)/2.0)))
    else:
        # upper (B/R)
        if len(seat) == 1:
            return upper
        return get_row_col_id(seat[1:], lower + int(math.ceil((upper-lower)/2.0)), upper)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(get_highest_seat_id(lines)))