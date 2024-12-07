#!/usr/bin/env python3


def parse_matrix(file):
    """Parse the input file in matrix format:"""
    """ABC"""
    """DEF"""
    """GHJ"""
    output = []
    for line in file.split('\n'):
        output.append(list(line))
    return output
