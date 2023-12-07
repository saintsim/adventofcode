#!/usr/bin/env python3

SEEDS = []
MAPS = []
SMALLEST = 0
SMALLEST_INTERVAL = 0

# 852082781


def parse(input):
    global SEEDS, SMALLEST, SMALLEST_INTERVAL, MAPS
    sections = input.split("\n\n")
    _, seeds_section = sections[0].split(":")
    seed_ranges = [int(s) for s in seeds_section.split()]
    SMALLEST = seed_ranges[0]
    for idx in range(0, len(seed_ranges), 2):
        if seed_ranges[idx] > 1000000000:
            continue
        SEEDS.append(seed_ranges[idx])
        for i in range(seed_ranges[idx]+1, min(9900000000, seed_ranges[idx] + seed_ranges[idx+1])):
            SEEDS.append(i)
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


def part2(input):
    parse(input)
    destinations = []
    for seed in SEEDS:
        if seed == 82:
            pass
        destination = seed
        for map in MAPS:
            for submap in map:
                if destination in submap[0]:
                    source_idx = submap[0].index(destination)
                    destination = submap[1][source_idx]
                    break
        if destination == 0:
            pass
        destinations.append(destination)
    return min(destinations)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
