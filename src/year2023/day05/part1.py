#!/usr/bin/env python3

SEEDS = []
MAPS = []


def parse(input):
    sections = input.split("\n\n")
    _, seeds_section = sections[0].split(":")
    global SEEDS
    SEEDS = [int(s) for s in seeds_section.split()]
    global MAPS
    for section in sections[1:]:
        _, tokens = section.split(":")
        section_values = tokens.split("\n")
        section_to_add = []
        for values in section_values:
            if values != "":
                range_tokens = [int(s) for s in values.split()]
                section_to_add.append([range(range_tokens[1], range_tokens[1]+range_tokens[2]),
                                       range(range_tokens[0], range_tokens[0]+range_tokens[2])])
        MAPS.append(section_to_add)


def part1(input):
    parse(input)
    destinations = []
    for seed in SEEDS:
        destination = seed
        for map in MAPS:
            for submap in map:
                if destination in submap[0]:
                    source_idx = submap[0].index(destination)
                    destination = submap[1][source_idx]
                    break
        destinations.append(destination)
    return min(destinations)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
