#!/usr/bin/env python3

LIFT_MAZE = []
ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]


def parse(input):
    lines = input.split('\n')
    for line in lines:
        maze_line = []
        for token in line:
            maze_line.append(token)
        LIFT_MAZE.append(maze_line)


def is_part_cell(point):
    if point[0] < 0 or point[1] < 0 or point[0] >= len(LIFT_MAZE) or point[1] >= len(LIFT_MAZE[0]):
        # off grid
        return False
    maze_point = LIFT_MAZE[point[0]][point[1]]
    return maze_point.isdigit()


def get_number_for_cell(coord):
    # go left and right to get this full number
    left_most_point = ()
    for i in range(len(LIFT_MAZE[0])):
        new_coord = (coord[0], coord[1]-i)
        if is_part_cell(new_coord):
            left_most_point = new_coord
        else:
            # reached the end
            break
    part_num = ''
    for i in range(len(LIFT_MAZE[0])):
        new_coord = (left_most_point[0], left_most_point[1] + i)
        if is_part_cell(new_coord):
            part_num += LIFT_MAZE[new_coord[0]][new_coord[1]]
        else:
            break
    return part_num


def get_part_neighbours(x,y):
    neighbours = set()
    for adj_coord in ADJACENT:
        new_point = (adj_coord[0]+x, adj_coord[1]+y)
        if is_part_cell(new_point):
            cell_number = get_number_for_cell(new_point)
            neighbours.add(cell_number)
    return neighbours


def get_part_numbers():
    total = []
    for x, line in enumerate(LIFT_MAZE):
        # find a sequence of numbers, then we can check if valid
        for y, token in enumerate(line):
            if token == '*':
                neighbours = get_part_neighbours(x, y)
                if len(neighbours) == 2:
                    total.append(int(neighbours.pop()) * int(neighbours.pop()))
    return total


def lift(input):
    parse(input)
    res = get_part_numbers()
    print(res)
    return sum(res)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(lift(file.read())))
