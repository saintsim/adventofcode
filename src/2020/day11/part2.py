#!/usr/bin/env python3

from src.day11.part1 import occupied_count, print_map, EMPTY, OCCUPIED, FLOOR

END = '|'


def waiting_area(seat_map, print_steps):
    round = 0
    while True:
        new_seat_map = generate_new_seat_map_part2(seat_map)
        if print_steps:
            print(round)
            print_map(new_seat_map)
        if new_seat_map == seat_map:
            break
        seat_map = new_seat_map
        round += 1
    return occupied_count(seat_map)


def generate_new_seat_map_part2(seat_map):
    new_seat_map = []
    for x, line in enumerate(seat_map):
        new_row = []
        for y, cell in enumerate(line):
            new_row.append(new_value_part2(x, y, seat_map))
        new_seat_map.append(new_row)
    return new_seat_map


def new_value_part2(x, y, seat_map):
    # ABC  --> y
    # D$E  |
    # FGH  \/  x
    current = seat_map[x][y]
    if current == EMPTY:
        pass
    if current == FLOOR:
        return FLOOR
    # head in each direction until you hit the END or an occupied seat
    directions = [
        lambda x, y: (x-1, y-1),  # a
        lambda x, y: (x-1, y),      # b
        lambda x, y: (x-1, y+1),  # c
        lambda x, y: (x, y-1),      # d
        lambda x, y: (x, y+1),      # e
        lambda x, y: (x+1, y-1),  # f
        lambda x, y: (x+1, y),      # g
        lambda x, y: (x+1, y+1)   # h
    ]
    occupied_count = 0
    for direction in directions:
        new_x, new_y = x, y
        while True:
            new_x, new_y = direction(new_x, new_y)
            cell_contents = cell_value(new_x, new_y, seat_map)
            if cell_contents == END:
                break
            elif cell_contents == OCCUPIED:
                occupied_count += 1
                break
    if current == EMPTY and occupied_count == 0:
        return OCCUPIED
    if current == OCCUPIED and occupied_count >= 5:
        return EMPTY
    return current


def cell_value(x, y, seat_map):
    if x < 0 \
            or x >= len(seat_map) \
            or y < 0 or y >= len(seat_map[0]) \
            or seat_map[x][y] == EMPTY:
        return END
    return seat_map[x][y]


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(waiting_area(lines, False)))
