#!/usr/bin/env python3

             # UP,      DOWN,    LEFT,   RIGHT
DIRECTIONS = [ (-1, 0), (1, 0), (0, -1), (0, 1)]
ALL_PATHS = []


def parse(input):
    output = []
    for line in input.split('\n'):
        output.append([None if x == '.' else int(x) for x in line])
    return output


def off_grid(maze, location):
    return location[0] < 0 or location[1] < 0 or location[0] > len(maze)-1 or location[1] > len(maze[0])-1


def get_paths(maze, start, current_number, visited):
    visited[current_number] = start
    if current_number == 9:
        ALL_PATHS.append(visited)
    print('Current: ' + str(current_number) + ', location: ' + str(start))
    for direction in DIRECTIONS:
        next_spot = (start[0] + direction[0], start[1] + direction[1])
        if off_grid(maze, next_spot):
            continue
        next_spot_number = maze[next_spot[0]][next_spot[1]]
        if next_spot_number is None:
            continue
        if next_spot_number == current_number + 1:
            get_paths(maze, next_spot, current_number+1, dict(visited))


def find_paths(maze, start_spots, end_spots):
    count = 0
    for start in start_spots:
        global ALL_PATHS
        ALL_PATHS = []
        get_paths(maze, start, 0, {})
        end_spots_seen = set()
        new_count = 0
        for paths_seen in ALL_PATHS:
            if len(paths_seen) != 10:
                continue
            if paths_seen[9] not in end_spots_seen:
                new_count += 1
                end_spots_seen.add(paths_seen[9])
        print('-> new: ' + str(new_count))
        count += new_count
    return count


def part1(input):
    maze = parse(input)
    # find the 0's and the 9's
    start_spots = set()
    end_spots = set()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 0:
                start_spots.add((y, x))
            elif cell == 9:
                end_spots.add((y, x))
    return find_paths(maze, start_spots, end_spots)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
