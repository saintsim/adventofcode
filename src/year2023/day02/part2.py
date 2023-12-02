#!/usr/bin/env python3


def part2(lines):
    total_per_set = []
    for line in lines:
        game, cubes = line.split(':')
        game_num = int(game.replace("Game ", ""))
        sub_games = cubes.split('; ')
        max_blue, max_red, max_green = 0, 0, 0
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
            if blue_count > max_blue:
                max_blue = blue_count
            if red_count > max_red:
                max_red = red_count
            if green_count > max_green:
                max_green = green_count
        total_per_set.append(max_green * max_red * max_blue)

    return sum(total_per_set)

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(part2(lines))
