#!/usr/bin/env python3

from src.day07.part1 import parse, BAGS

RESULT = 0


def individual_bag_size(lines, colour_to_find):
    parse(lines)
    get_individual_bag_count(colour_to_find, 1)
    return RESULT


def get_individual_bag_count(colour, qty):
    for matched_colour, matched_colour_qty in BAGS[colour].directly_contains.items():
        global RESULT
        RESULT += matched_colour_qty * qty
        if matched_colour in BAGS:
            get_individual_bag_count(matched_colour, matched_colour_qty * qty)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(individual_bag_size(lines, 'shiny gold')))
