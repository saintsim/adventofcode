#!/usr/bin/env python3

from libraries.parsing.matrix import parse_matrix

MATRIX = []
WALL = '#'
DIRECTIONS = ['U', 'R', 'D', 'L']
DIRECTION_MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def off_map(position):
    return position[0] < 0 or position[0] > len(MATRIX)-1 or position[1] < 0 or position[1] > len(MATRIX[0])-1


def do_walk(walls, start, direction_index):
    current_position = start
    visited = set()
    visited.add(current_position)
    direction_for_visited = {current_position: [direction_index]}
    print(current_position)
    while True:
        next_move = (current_position[0]+DIRECTION_MOVES[direction_index][0],
                     current_position[1]+DIRECTION_MOVES[direction_index][1])
        if off_map(next_move):
            return visited, False
        if (next_move in visited) and (direction_index in direction_for_visited[next_move]):
            pass
            return visited, True
        if next_move in walls:
            # hit obstacle
            direction_index = (direction_index+1) % len(DIRECTION_MOVES)
        else:
            current_position = next_move
            print(current_position)
            if current_position in visited:
                pass
            visited.add(current_position)
            direction_for_visited.setdefault(current_position, []).append(direction_index)


def get_walls_and_start():
    walls = {}
    start = None
    for idx_y, col in enumerate(MATRIX):
        for idx_x, row in enumerate(col):
            if row == '#':
                walls[(idx_y, idx_x)] = WALL
            elif row == "^":
                start = (idx_y, idx_x)
    return walls, start


def part2(input):
    global MATRIX
    MATRIX = parse_matrix(input)
    # record the map points
    direction_index = 0
    walls, start = get_walls_and_start()
    visited, _ = do_walk(walls, start, direction_index)
    visited.remove(start)
    # now block each
    infinite_combinations_count = 0
    i = 0
    for new_wall in visited:
        print('-> On item: ' + str(i) + ' of ' + str(len(visited)) + ': ' + str(new_wall))
        new_walls = dict(walls)
        new_walls[new_wall] = WALL
        _, is_infinite = do_walk(new_walls, start, direction_index)
        if is_infinite:
            infinite_combinations_count += 1
        i += 1
    return infinite_combinations_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
