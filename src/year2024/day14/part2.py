#!/usr/bin/env python3

import re
from libraries.print.PrintColours import PrintColours

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


def get_neighbours(robots):
    return [
        (robots[0]-1, robots[1]-1),
        (robots[0]-1, robots[1]),
        (robots[0]-1, robots[1]+1),
        (robots[0],   robots[1]-1),
        (robots[0],   robots[1]+1),
        (robots[0]+1, robots[1]-1),
        (robots[0]+1, robots[1]),
        (robots[0]+1, robots[1]+1)
    ]


def has_neighbours(robots, grid):
    neighbour_count = len(robots)
    for robot in robots:
        pos = robot[POS]
        has_a_neighbour = False
        for neighbour in get_neighbours(pos):
            if off_grid(neighbour):
                continue
            if grid[neighbour[0]][neighbour[1]] != 0:
                has_a_neighbour = True
                break
        if not has_a_neighbour:
            neighbour_count -= 1
    perc = ((neighbour_count / len(robots)) * 100)
    print('Perc = ' + str(perc))
    return perc > 65


def print_grid(robots, i):
    interesting = False
    grid = []
    for _ in range(BOARD_SIZE[0]):
        new_row = []
        for _ in range(BOARD_SIZE[1]):
            new_row.append(0)
        grid.append(new_row)

    # make grid
    for robot in robots:
        pos = robot[POS]
        grid[pos[0]][pos[1]] += 1

    if has_neighbours(robots, grid):
        interesting = True

    # for y in range(BOARD_SIZE[0]):
    #     count = 0
    #     for x in range(BOARD_SIZE[1]):
    #         if grid[y][x] != 0:
    #             count += 1
    #     if count > 40:
    #         interesting = True

    if interesting:
        print('i =' + str(i))
        for y in range(BOARD_SIZE[0]):
            for x in range(BOARD_SIZE[1]):
                if grid[y][x] != 0:
                    print(f"{PrintColours.OKGREEN}" + str(grid[y][x]) + f"{PrintColours.ENDC}", end='')
                else:
                    print(f"{PrintColours.BLACK}" + str(grid[y][x]) + f"{PrintColours.ENDC}", end='')
            print('')
        print('')
        print('----')
        print('')


def part1(input):
    robots = parse(input)
    i = 0
    while True:
        for idx, robot in enumerate(robots):
            robot_updated_position = update_position(robot)
            robots[idx] = robot_updated_position
        i += 1
        print('i =' + str(i))
        print_grid(robots, i)
        if i > 200000:
            return
        # if tree, return


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
