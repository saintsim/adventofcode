#!/usr/bin/env python3

from src.day24.part1 import parse, run, count_black, TILES, next_tile, Tile


def lobby2(lines):
    token_lines = parse(lines)
    run(token_lines)
    for _ in range(100):
        art_flip()
    return count_black()


def art_flip():
    new_tiles = dict()
    for x in TILES:
        for y in TILES[x]:
            adjacent_tiles = get_adjacent_tiles(x, y)
            adjacent_colours = get_adjacent_colours(adjacent_tiles)
            black_count = adjacent_colours.count('black')
            if TILES[x][y].colour == 'black':
                if black_count == 0 or black_count > 2:
                    TILES[x][y].art_flip_colour = 'white'
            else:
                if black_count == 2:
                    TILES[x][y].art_flip_colour = 'black'
            # check if adjacent tiles are in scope
            for adjacent_tile_x, adjacent_tile_y in adjacent_tiles:
                if adjacent_tile_x not in TILES or adjacent_tile_y not in TILES[adjacent_tile_x]:
                    adjacent_tiles_l2 = get_adjacent_tiles(adjacent_tile_x, adjacent_tile_y)
                    adjacent_colours_l2 = get_adjacent_colours(adjacent_tiles_l2)
                    if adjacent_colours_l2.count('black') == 2:
                        if adjacent_tile_x not in new_tiles:
                            new_tiles[adjacent_tile_x] = dict()
                        new_tiles[adjacent_tile_x][adjacent_tile_y] = Tile()
    # now perform the flip
    for x in TILES:
        for y in TILES[x]:
            tile = TILES[x][y]
            if tile.art_flip_colour != '':
                TILES[x][y].colour = tile.art_flip_colour
                TILES[x][y].art_flip_colour = ''
    # add in the new tiles
    for new_x in new_tiles:
        for new_y in new_tiles[new_x]:
            if new_x not in TILES:
                TILES[new_x] = dict()
            TILES[new_x][new_y] = new_tiles[new_x][new_y]


def get_adjacent_colours(adjacent_tiles):
    colours = []
    for next_x, next_y in adjacent_tiles:
        colours.append(next_tile_colour(next_x, next_y))
    return colours


def get_adjacent_tiles(x, y):
    adjacent_tiles = []
    for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
        adjacent_tiles.append(next_tile(x, y, direction))
    return adjacent_tiles


def next_tile_colour(x, y):
    if x in TILES and y in TILES[x]:
        return TILES[x][y].colour
    return 'white'


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(lobby2(lines)))
