#!/usr/bin/env python3

import re
import math

POS = 'position'
VEL = 'velocity'
BOARD_SIZE = (103, 101)


# (7, 11)


def parse(input):
    robots = []
    for line in input.split('\n'):
        px, py, vx, vy = re.findall(r'(-?\d+)', line)
        robots.append({POS: (int(py), int(px)), VEL: (int(vy), int(vx))})
    return robots


def off_grid(position):
    if position[0] < 0 or position[1] < 0 or position[0] > BOARD_SIZE[0] - 1 or position[1] > BOARD_SIZE[1] - 1:
        return True


def get_wrapped_position(position):
    new_position = (position[0] % BOARD_SIZE[0], position[1] % BOARD_SIZE[1])
    return new_position


def update_position(robot):
    new_position = (robot[POS][0] + robot[VEL][0], robot[POS][1] + robot[VEL][1])
    # is off grid? if so put back on
    if off_grid(new_position):
        new_position = get_wrapped_position(new_position)
    robot[POS] = new_position
    return robot


def get_score(robots):
    #  0 | 1
    #  2 | 3
    score_per_quad = [0, 0, 0, 0]
    for robot in robots:
        pos = robot[POS]
        middle_y = int(BOARD_SIZE[0] / 2)
        middle_x = int(BOARD_SIZE[1] / 2)
        if pos[0] == middle_y or pos[1] == middle_x:
            continue
        if pos[0] < middle_y and pos[1] < middle_x:
            score_per_quad[0] += 1
        elif pos[0] < middle_y and pos[1] > middle_x:
            score_per_quad[1] += 1
        elif pos[0] > middle_y and pos[1] < middle_x:
            score_per_quad[2] += 1
        else:
            score_per_quad[3] += 1
    return math.prod(score_per_quad)


def part1(input):
    robots = parse(input)
    for second in range(100):
        for idx, robot in enumerate(robots):
            robot_updated_position = update_position(robot)
            robots[idx] = robot_updated_position
    # scoring
    return get_score(robots)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
