#!/usr/bin/env python3

from src.day03.part1 import init_maze, traverse_maze


def maze_trees(lines):
    maze = init_maze(lines)
    return traverse_maze(maze, 1, 1) * traverse_maze(maze, 3, 1) * traverse_maze(maze, 5, 1) * traverse_maze(maze, 7, 1) * traverse_maze(maze, 1,2)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(maze_trees(lines)))