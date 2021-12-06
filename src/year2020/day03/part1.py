#!/usr/bin/env python3


def maze_trees(lines):
    return traverse_maze(init_maze(lines), 3, 1)


def traverse_maze(maze, x_change, y_change):
    #  x --->
    #        !
    #        \/
    #         y
    x, y, tree_count = 0, 0, 0
    while True:
        if y >= len(maze):
            return tree_count
        cell_contents = maze[y][x % len(maze[0])]
        if cell_contents is "#":
            tree_count += 1
        x += x_change
        y += y_change


def init_maze(lines):
    maze = []
    for line in lines:
        row = []
        for cell in line:
            row.append(cell)
        maze.append(row)
    return maze


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(maze_trees(lines)))