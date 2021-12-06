#!/usr/bin/env python3

import re

TILES = dict()
TILES_BY_SIDE = dict()


class Tile:
    def __init__(self, id, image):
        self.id = id
        self.image = image
        # sides: 0: top, 1: bottom, 2: left, 3: right
        #        4: top inverted, 5: bottom inverted, 6: left inverted, 7: right inverted
        self.sides = []
        self.calc_sides()
        self.sides_match = []

    def calc_sides(self):
        left, right = '', ''
        for line in self.image:
            left += line[0]
            right += line[-1]
        self.sides = [self.image[0], self.image[-1], left, right]
        # rotated versions too
        new_sides = []
        for side in self.sides:
            new_sides.append(side[::-1])
        self.sides += new_sides


def tiles(lines):
    parse(lines)
    populate_tiles_by_side()
    determine_matching_sides()
    corners = []
    for tile in TILES:
        if len(TILES[tile].sides_match) < 5:
            corners.append(int(tile[0]))
    if len(corners) > 4:
        Exception('We somehow have {} corners, rather than 4. Thats more corners than should exist!', str(len(corners)))
    return corners[0] * corners[1] * corners[2] * corners[3]


def determine_matching_sides():
    for side_id in TILES_BY_SIDE:
        side_tiles = TILES_BY_SIDE[side_id]
        if len(side_tiles) > 1:
            for match in side_tiles:
                TILES[match[0]].sides_match.append(match[1])


def populate_tiles_by_side():
    for tile_id in TILES:
        tile = TILES[tile_id]
        for side in range(len(tile.sides)):
            tile_side = tile.sides[side]
            if tile_side in TILES_BY_SIDE:
                TILES_BY_SIDE[tile_side].append((tile.id, side))
            else:
                TILES_BY_SIDE[tile_side] = [(tile.id, side)]


def parse(lines):
    i, tile_id, image = 0, 0, []
    while i < len(lines):
        current_line = lines[i].strip()
        if 'Tile' in current_line:
            if len(image):
                TILES[tile_id] = Tile(tile_id, image)
            tile_id = re.match(r'Tile (\d+):$', current_line).groups()
            image = []
        elif current_line != '':
            image.append(current_line)
        i += 1
    TILES[tile_id] = Tile(tile_id, image)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(tiles(lines)))
