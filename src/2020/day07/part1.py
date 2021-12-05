#!/usr/bin/env python3

import re

BAGS = dict()
MATCHES = set()


class Bag:
    def __init__(self, colour):
        self.colour = colour
        self.directly_contains = dict()
        self.directly_contained_by = set()

    def update_directly_contains(self, colour, qty):
        if colour in self.directly_contains:
            self.directly_contains[colour] += qty
        else:
            self.directly_contains[colour] = qty

    def __str__(self):
        return self.colour


def bag_colours(lines, colour_to_find):
    parse(lines)
    populate_containing_colour_matches(colour_to_find)
    return len(MATCHES)


def populate_containing_colour_matches(colour):
    for inner_bag_colour in BAGS[colour].directly_contained_by:
        print("Match: " + inner_bag_colour)
        MATCHES.add(inner_bag_colour)
        populate_containing_colour_matches(inner_bag_colour)
    
    
def parse(lines):
    for line in lines:
        bags = re.match('(.+) bags contain (.+).', line)
        if bags:
            outer_bag_colour, inner_bags = bags.groups()
            if outer_bag_colour not in BAGS:
                BAGS[outer_bag_colour] = Bag(outer_bag_colour)
            for inner_bag in inner_bags.split(','):
                inner_bags_matches = re.match('([0-9]*) (.+) bag', inner_bag.strip())
                if inner_bags_matches:
                    inner_bag_qty, inner_bag_colour = inner_bags_matches.groups()
                    BAGS[outer_bag_colour].update_directly_contains(inner_bag_colour, int(inner_bag_qty))
                    if inner_bag_colour in BAGS:
                        BAGS[inner_bag_colour].directly_contained_by.add(outer_bag_colour)
                    else:
                        new_inner_bag_entry = Bag(inner_bag_colour)
                        new_inner_bag_entry.directly_contained_by.add(outer_bag_colour)
                        BAGS[inner_bag_colour] = new_inner_bag_entry
                    print(str(outer_bag_colour + " contains: " + str(inner_bag_qty) + "x " + inner_bag_colour))


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(bag_colours(lines, 'shiny gold')))