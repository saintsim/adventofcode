#!/usr/bin/env python3

def parse_int_space(file):
    """Parse the input file in format on each line: 1 2 3"""
    output = []
    for line in file.split('\n'):
        output.append([int(x) for x in line.split()])
    return output


def parse_int_colon_space(file):
    """Parse the input file in format on each line: 10: 1 2 3"""
    output = []
    for line in file.split('\n'):
        total, values = line.split(': ')
        output.append((int(total), [int(x) for x in values.split()]))
    return output
