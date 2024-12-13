#!/usr/bin/env python3

import re
import math

def parse(input):
    games_input = input.split('\n\n')
    games = []
    for game in games_input:
        button_a, button_b, prize = game.split('\n')
        games.append({
            'button_a': get_x_y(button_a, '\+'),
            'button_b': get_x_y(button_b, '\+'),
            'prize': get_x_y(prize, '\=')
        })
    return games


def get_x_y(line, delim):
    coords = re.findall(delim + '(\d+)', line)
    return int(coords[0]), int(coords[1])


def can_win(game):
    # 3 tokens to push the A button
    # 1 token to push the B button.
    button_a = game['button_a']
    button_b = game['button_b']
    prize = game['prize']

    # max push needed
    button_a_max = max(math.ceil(prize[0] / button_a[0]), math.ceil(prize[1] / button_a[1]))
    button_b_max = max(math.ceil(prize[0] / button_b[0]), math.ceil(prize[1] / button_b[1]))

    min_cost = None

    for a_push_times in range(button_a_max):
        for b_push_times in range(button_b_max):
            if prize[0] != (a_push_times * button_a[0] + b_push_times * button_b[0]):
                continue
            if prize[1] != (a_push_times * button_a[1] + b_push_times * button_b[1]):
                continue
            cost = (a_push_times * 3) + b_push_times
            if min_cost is None or cost < min_cost:
                min_cost = cost
    return 0 if min_cost is None else min_cost


def part1(input):
    games = parse(input)
    count = 0
    for game in games:
        count += can_win(game)
    return count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
