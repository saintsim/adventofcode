#!/usr/bin/env python3


def get_highest_seat_id(lines):
    highest_seat_id = 0
    for line in lines:
        seat_id = get_seat_id(line)
        highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id
    return highest_seat_id


def get_seat_id(seat):
    seat = seat.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1")
    return int(seat, 2)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(get_highest_seat_id(lines)))