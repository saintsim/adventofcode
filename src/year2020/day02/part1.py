#!/usr/bin/env python3

import re


def password_checker(lines):
    valid_password_count = 0
    for line in lines:
        valid_password_count += password_is_valid(line)
    return valid_password_count


def password_is_valid(line):
    min_amount, max_amount, char_to_check, password = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line).groups()
    return int(min_amount) <= password.count(char_to_check) <= int(max_amount)


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(password_checker(lines)))
