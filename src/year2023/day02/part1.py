#!/usr/bin/env python3


def part1(lines):
    valid_games = set()
    for line in lines:
        game, cubes = line.split(':')
        game_num = int(game.replace("Game ", ""))
        sub_games = cubes.split('; ')
        max_blue, max_red, max_green = 14, 12, 13
        valid_game = True
        for sub_game in sub_games:
            blue_count, red_count, green_count = 0, 0, 0
            cube_colours = sub_game.split(', ')
            for cube_colour in cube_colours:
                num, _ = cube_colour.strip().split(' ')
                if 'blue' in cube_colour:
                    blue_count = int(num)
                elif 'green' in cube_colour:
                    green_count = int(num)
                else:
                    red_count = int(num)
            if blue_count > max_blue or red_count > max_red or green_count > max_green:
                valid_game = False
                break
        if valid_game:
            print('Game is valid: ', game_num)
            valid_games.add(game_num)
    return sum(valid_games)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(part1(lines))
