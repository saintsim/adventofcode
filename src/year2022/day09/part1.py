#!/usr/bin/env python3

HEAD_POSITIONS = [(0, 0)]
TAIL_POSITIONS = [(0, 0)]


def move_tail(head_x, head_y):
    current_tail_x, current_tail_y = TAIL_POSITIONS[-1]
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
    TAIL_POSITIONS.append((current_tail_x, current_tail_y))


def make_move(direction, movement):
    current_x, current_y = HEAD_POSITIONS[-1]
    for _ in range(movement):
        if direction == 'L':
            current_x -= 1
        elif direction == 'R':
            current_x += 1
        elif direction == 'U':
            current_y += 1
        else:
            current_y -= 1
        HEAD_POSITIONS.append((current_x, current_y))
        move_tail(current_x, current_y)


def follow_the_tail(input):
    for line in input:
        direction, movement = line.split()
        make_move(direction, int(movement))
    return len(set(TAIL_POSITIONS))


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(follow_the_tail(lines)))