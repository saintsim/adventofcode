#!/usr/bin/env python3

import re


# noinspection PyShadowingNames
def password_checker(lines):
    valid_password_count = 0
    for line in lines:
        if password_is_valid(line):
            valid_password_count += 1
    return valid_password_count


def password_is_valid(line):
    position_a, position_b, char_to_check, password = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line).groups()
    has_a = password[int(position_a)-1] is char_to_check
    has_b = password[int(position_b) - 1] is char_to_check
    return has_a ^ has_b  # bitwise exclusive or


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(password_checker(lines)))
