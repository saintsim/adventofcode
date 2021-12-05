#!/usr/bin/env python3

from src.day05.part1 import get_seat_id


def get_highest_seat_id(lines):
    seat_ids = []
    for line in lines:
        seat_ids.append(get_seat_id(line))
    seat_ids.sort()
    full_list = range(seat_ids[0], seat_ids[0]+len(seat_ids)+1)
    return set(full_list)-set(seat_ids)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(get_highest_seat_id(lines)))