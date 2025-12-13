#!/usr/bin/env python3

def new_beam_location(point):
    return point[0] + 1, point[1]


def part1(input):
    split_count = 0
    world = [list(line) for line in input.split('\n')]
    # we know S is on the first line
    s_location = (0, world[0].index('S'))
    beams = []
    for line in world[1:]:
        if '^' not in line:
            if not beams:
                beams = [[new_beam_location(s_location)]]
            else:
                new_beams = set()
                for beam in beams[len(beams)-1]:
                    new_beams.add(new_beam_location(beam))
                beams.append(new_beams)
        else:
            new_beams = set()
            for beam in beams[len(beams) - 1]:
                next_beam_location = new_beam_location(beam)
                if line[next_beam_location[1]] == '.':
                    new_beams.add(next_beam_location)
                else:
                    split_count += 1
                    new_beams.add((next_beam_location[0], next_beam_location[1]-1))
                    new_beams.add((next_beam_location[0], next_beam_location[1]+1))
            beams.append(new_beams)
    return split_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
