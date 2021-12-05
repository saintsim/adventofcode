#!/usr/bin/env python3

EMPTY, OCCUPIED, FLOOR = 'L', '#', '.'


def waiting_area(seat_map):
    round = 0
    while True:
        print(round)
        new_seat_map = generate_new_seat_map(seat_map)
        if new_seat_map == seat_map:
            break
        seat_map = new_seat_map
        round += 1
    return occupied_count(seat_map)


def print_map(seat_map):
    for row in seat_map:
        print(row)


def occupied_count(seat_map):
    return sum([row.count(OCCUPIED) for row in seat_map])


def generate_new_seat_map(seat_map):
    new_seat_map = []
    for x, line in enumerate(seat_map):
        new_row = []
        for y, cell in enumerate(line):
            new_row.append(new_value(x, y, seat_map))
        new_seat_map.append(new_row)
    return new_seat_map


def new_value(x, y, seat_map):
    # ABC  --> y
    # D.E  |
    # FGH  \/  x
    current = seat_map[x][y]
    if current == '.':
        return current
    adjacent_cells = [
        cell_value(x-1, y-1, seat_map),  # a
        cell_value(x-1, y, seat_map),    # b
        cell_value(x-1, y+1, seat_map),  # c
        cell_value(x, y-1, seat_map),    # d
        cell_value(x, y+1, seat_map),    # e
        cell_value(x+1, y-1, seat_map),  # f
        cell_value(x+1, y, seat_map),    # g
        cell_value(x+1, y+1, seat_map)   # h
    ]
    occupied_count = adjacent_cells.count(OCCUPIED)
    if current == EMPTY and occupied_count == 0:
        return OCCUPIED
    if current == OCCUPIED and occupied_count >= 4:
        return EMPTY
    return current


def cell_value(x, y, seat_map):
    if x < 0 or x >= len(seat_map) or y < 0 or y >= len(seat_map[0]):
        return FLOOR
    return seat_map[x][y]


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(waiting_area(lines)))
