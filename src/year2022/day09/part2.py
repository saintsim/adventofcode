#!/usr/bin/env python3

SNAKE = []


def move_knot(idx, head_x, head_y):
    current_tail_x, current_tail_y = SNAKE[idx][-1]
    x_diff = head_x - current_tail_x
    y_diff = head_y - current_tail_y
    # If the head is ever two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough:
    if head_x == current_tail_x and head_y == current_tail_y:
        pass
    elif head_x == current_tail_x:
        if abs(y_diff) > 1:
            current_tail_y += 1 if y_diff > 0 else -1
    elif head_y == current_tail_y:
        if abs(x_diff) > 1:
            current_tail_x += 1 if x_diff > 0 else -1
    elif head_x == current_tail_x and head_y == current_tail_y:
        pass
    else:
        # diaganol
        # Otherwise, if the head and tail aren't touching and aren't in the same row or column,
        # the tail always moves one step diagonally to keep up:
        if abs(x_diff) > 1 or abs(y_diff) > 1:
            current_tail_x += 1 if x_diff > 0 else -1
            current_tail_y += 1 if y_diff > 0 else -1
    SNAKE[idx].append((current_tail_x, current_tail_y))


def make_move(direction, movement):
    # init
    current_x, current_y = SNAKE[0][-1]
    for _ in range(movement):
        if direction == 'L':
            current_x -= 1
        elif direction == 'R':
            current_x += 1
        elif direction == 'U':
            current_y += 1
        else:
            current_y -= 1
        SNAKE[0].append((current_x, current_y))
        for i in range(9):
            prev_knot_x, prev_knot_y = SNAKE[i][-1]
            move_knot(i+1, prev_knot_x, prev_knot_y)


def follow_the_leader(input):
    for _ in range(10):
        SNAKE.append([(0, 0)])
    for line in input:
        direction, movement = line.split()
        make_move(direction, int(movement))
    return len(set(SNAKE[-1]))


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(follow_the_leader(lines)))