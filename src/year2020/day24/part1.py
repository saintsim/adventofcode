#!/usr/bin/env python3

import re

TILES = dict()


class Tile:
    def __init__(self):
        self.colour = 'black'
        self.art_flip_colour = ''
        self.flip_count = 0

    def flip(self, x, y):
        before = str(self.colour)
        self.colour = 'black' if self.colour == 'white' else 'white'
        self.flip_count += 1
        print('flipping ' + str(x) + ', ' + str(y) + ' from: ' + before + ', to: ' + self.colour)


def next_tile(x, y, direction):
    if direction == 'e':
        return x+2, y
    elif direction == 'w':
        return x-2, y
    elif direction == 'se':
        return x+1, y+1
    elif direction == 'sw':
        return x-1, y+1
    elif direction == 'ne':
        return x+1, y-1
    elif direction == 'nw':
        return x-1, y-1
    else:
        raise Exception('unknown direction')


def lobby(lines):
    token_lines = parse(lines)
    run(token_lines)
    return count_black()


def count_black():
    black = 0
    print('==== BLACK TILES ====')
    tile_count = 0
    for x in TILES:
        for y in TILES[x]:
            tile_count += 1
            if TILES[x][y].colour == 'black':
                print(str(x) + ', ' + str(y) + '; flip count: ' + str(TILES[x][y].flip_count))
                black += 1
    return black


def parse(lines):
    token_lines = []
    for line in lines:
        token_lines.append(re.findall('(e|se|sw|w|nw|ne)', line))
    return token_lines


def run(token_lines):
    for token_line in token_lines:
        x, y = 0, 0
        for token in token_line:
            x, y = next_tile(x, y, token)
        if x in TILES:
            if y in TILES[x]:
                TILES[x][y].flip(x, y)
                continue
        else:
            TILES[x] = dict()
        TILES[x][y] = Tile()


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(lobby(lines)))
