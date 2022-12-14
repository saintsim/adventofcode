#!/usr/bin/env python3

# spare grid of tuple of x,y's
ROCK, SAND, AIR = '#', '0', '.'
HEIGHT_OF_GRID = 0
SAND_COUNT = 0
GRID = dict()

# from part 1


def tup_to_int(point):
    return int(point[0]), int(point[1])


def update_height(y1, y2):
    global HEIGHT_OF_GRID
    HEIGHT_OF_GRID = max(y1, y2, HEIGHT_OF_GRID)


def populate_rock(points1, points2):
    print(points1, points2)
    update_height(points1[1], points2[1])
    if points1[0] == points2[0]:
        for y in range(min(points1[1], points2[1]), max(points1[1], points2[1])+1):
            GRID[points1[0], y] = ROCK
    elif points1[1] == points2[1]:
        for x in range(min(points1[0], points2[0]), max(points1[0], points2[0])+1):
            GRID[x, points1[1]] = ROCK
    else:
        print('ouch, not supported...', points1, points2)
        pass


def parse(input):
    # where x represents distance to the right and y represents distance down
    # 498,4 -> 498,6 -> 496,6
    # x,y
    for line in input:
        points = []
        for section in line.split('->'):
            points.append(section.split(','))
        i = 1
        for current_points in points[1:]:
            populate_rock(tup_to_int(points[i-1]), tup_to_int(current_points))
            i += 1


# part 2 logic


def in_grid(point):
    if point in GRID and (GRID[point] == ROCK or GRID[point] == SAND):
        return True
    if point[1] == HEIGHT_OF_GRID+2:
        return True
    return False


def flow_sand():
    global SAND_COUNT
    while True:
        current_sand_point = (500, 0)
        while current_sand_point[1] <= HEIGHT_OF_GRID+3:
            below = (current_sand_point[0], current_sand_point[1]+1)
            if in_grid(below):
                below_left = (current_sand_point[0]-1, current_sand_point[1]+1)
                if in_grid(below_left):
                    below_right = (current_sand_point[0] + 1, current_sand_point[1] + 1)
                    if in_grid(below_right):
                        GRID[current_sand_point] = SAND
                        SAND_COUNT += 1
                        break
                    else:
                        current_sand_point = below_right
                else:
                    current_sand_point = below_left
            else:
                current_sand_point = below

        if (500, 0) in GRID and GRID[(500, 0)] == SAND:
            break


def sand(input):
    parse(input)
    flow_sand()
    return SAND_COUNT


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(sand(lines)))