#!/usr/bin/env python3

from src.day12.part1 import manhattan


def navigation(lines):
    waypoint_x = 10
    waypoint_y = -1
    ship_x, ship_y = 0, 0
    for line in lines:
        print(line)
        direction = line[0]
        value = int(line[1:])
        if direction == 'N':
            waypoint_y -= value
        elif direction == 'S':
            waypoint_y += value
        elif direction == 'E':
            waypoint_x += value
        elif direction == 'W':
            waypoint_x -= value
        elif direction == 'L':
            previous_waypoint_x = waypoint_x
            if value == 90:
                waypoint_x = waypoint_y
                waypoint_y = previous_waypoint_x * -1
            elif value == 180:
                waypoint_x *= -1
                waypoint_y *= -1
            elif value == 270:
                waypoint_x = waypoint_y * -1
                waypoint_y = previous_waypoint_x
        elif direction == 'R':
            previous_waypoint_x = waypoint_x
            if value == 90:
                waypoint_x = waypoint_y * -1
                waypoint_y = previous_waypoint_x
            elif value == 180:
                waypoint_x *= -1
                waypoint_y *= -1
            elif value == 270:
                waypoint_x = waypoint_y
                waypoint_y = previous_waypoint_x * -1
        elif direction == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
        print('Waypoint: x:{}, y:{}', waypoint_x, waypoint_y)
        print('Ship: x:{}, y:{}', ship_x, ship_y)
    return manhattan(0, 0, ship_x, ship_y)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(navigation(lines)))