#!/usr/bin/env python3

def navigation(lines):
    x, y, current_direction = 0, 0, 0
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        if direction == 'N':
            y -= value
        elif direction == 'S':
            y += value
        elif direction == 'E':
            x += value
        elif direction == 'W':
            x -= value
        elif direction == 'L':
            current_direction = (current_direction - value) % 360
        elif direction == 'R':
            current_direction = (current_direction + value) % 360
        elif direction == 'F':
            if current_direction == 0:
                x += value
            elif current_direction == 90:
                y += value
            elif current_direction == 180:
                x -= value
            elif current_direction == 270:
                y -= value
    return manhattan(0, 0, x, y)


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(navigation(lines)))