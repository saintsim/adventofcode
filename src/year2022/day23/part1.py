#!/usr/bin/env python3


DIRECTIONS = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0),
              'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
MAP = dict()
PROPOSED_MOVES = dict()


class Elf:

    def __init__(self, id, current_cell, move_directions):
        self.id = id
        self.move_directions = move_directions
        self.current_cell = current_cell
        self.proposed_move_direction = None

    def append_considered_to_end(self):
        self.move_directions.append(self.move_directions.pop(0))


def add_tuple(t1, t2):
    return t1[0]+t2[0], t1[1]+t2[1]


def find_elves_to_move():
    elves_to_move = set()
    for elf in MAP.values():
        for dir in DIRECTIONS.values():
            proposed_move = add_tuple(elf.current_cell, dir)
            if proposed_move in MAP:
                elves_to_move.add(elf)
                break
    return elves_to_move


def find_proposed_move_for_dir(elf, d1, d2, d3):
    d1_cell = add_tuple(elf.current_cell, DIRECTIONS[d1])
    d2_cell = add_tuple(elf.current_cell, DIRECTIONS[d2])
    d3_cell = add_tuple(elf.current_cell, DIRECTIONS[d3])
    if d1_cell not in MAP and d2_cell not in MAP and d3_cell not in MAP:
        if d1_cell in PROPOSED_MOVES:
            PROPOSED_MOVES[d1_cell].append(elf)
        else:
            PROPOSED_MOVES[d1_cell] = [elf]
        return True


def find_proposed_moves(elves_to_move):
    global PROPOSED_MOVES
    PROPOSED_MOVES = dict()
    for elf in elves_to_move:
        for dir in elf.move_directions:
            if dir == 'N':
                if find_proposed_move_for_dir(elf, 'N', 'NE', 'NW'):
                    elf.proposed_move_direction = 'N'
                    break
            elif dir == 'S':
                if find_proposed_move_for_dir(elf, 'S', 'SE', 'SW'):
                    elf.proposed_move_direction = 'S'
                    break
            elif dir == 'W':
                if find_proposed_move_for_dir(elf, 'W', 'NW', 'SW'):
                    elf.proposed_move_direction = 'W'
                    break
            else:
                if find_proposed_move_for_dir(elf, 'E', 'NE', 'SE'):
                    elf.proposed_move_direction = 'E'
                    break


def do_round():
    elves_to_move = find_elves_to_move()
    if len(elves_to_move) == 0:
        return False
    find_proposed_moves(elves_to_move)
    for proposed_move, elves in PROPOSED_MOVES.items():
        if len(elves) == 1:
            elf = elves[0]
            # they get their move
            # update the elves current cell, update their move directions
            prev_cell = elf.current_cell
            elf.current_cell = proposed_move
            # remove them from the current cell in MAP, add them to the new cell
            del MAP[prev_cell]
            MAP[proposed_move] = elf
    for elf in MAP.values():
        elf.append_considered_to_end()
    return True


def draw_map():
    groud_cells = 0
    smallest_x = min([k[0] for k in MAP.keys()])
    smallest_y = min([k[1] for k in MAP.keys()])
    biggest_x = max([k[0] for k in MAP.keys()])
    biggest_y = max([k[1] for k in MAP.keys()])
    for y in range(smallest_y, biggest_y+1):
        for x in range(smallest_x, biggest_x + 1):
            if (x,y) in MAP:
                print('#', end='')
            else:
                print('.', end='')
                groud_cells += 1
        print()
    return groud_cells


def tiles(input):
    id = 0
    for y, line in enumerate(input):
        for x, cell in enumerate(line):
            if cell == '#':
                MAP[(x,y)] = Elf(id, (x,y), ['N', 'S', 'W', 'E'])
                id += 1
    ground_cells = 0
    print('== Initial state ==')
    draw_map()
    print('')
    for round in range(1000000):
        print('== End of Round: ', round+1, ' ==')
        if do_round() is False:
            return round+1
        #ground_cells = draw_map()
        print('')
        pass
    return ground_cells


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(tiles(lines))
