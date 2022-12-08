#!/usr/bin/env python3

SCENIC_SCORE_GRID = None
GRID = []
GRID_SIZE = 0


def visible_score_for_direction(x, y, move_x, move_y):
    current_height = GRID[y][x]
    score = 0
    while True:
        x += move_x
        y += move_y
        if x < 0 or y < 0 or x > GRID_SIZE - 1 or y > GRID_SIZE - 1:
            break
        next_height = GRID[y][x]
        if next_height >= current_height:
            return score + 1
        score += 1
    return score


def visible_score(x, y):
    print(x, y)
    if x == 0 or y == 0 or x == GRID_SIZE - 1 or y == GRID_SIZE - 1:
        return 0
    #       X   Y
    # up:   0   -1
    # down: 0   1
    # left  -1  0
    # right 1   0
    return visible_score_for_direction(x, y, 0, -1) * visible_score_for_direction(x, y, 0, 1) * \
           visible_score_for_direction(x, y, -1, 0) * visible_score_for_direction(x, y, 1, 0)


def grid(input):
    global GRID_SIZE, SCENIC_SCORE_GRID
    GRID_SIZE = len(input[0])
    SCENIC_SCORE_GRID = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
    scores = []
    for line in input:
        GRID.append(list(line))
    for y, row in enumerate(GRID):
        for x, cell in enumerate(row):
            cell_score = visible_score(x, y)
            print(y, x, "->", cell_score)
            SCENIC_SCORE_GRID[y][x] = cell_score
            scores.append(cell_score)
    return max(scores)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(grid(lines)))
