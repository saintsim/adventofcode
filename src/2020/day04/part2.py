#!/usr/bin/env python3

import re


def passport_check(lines):
    passports = parse_passport_data(lines)
    valid_passports = 0
    for passport in passports:
        if valid_passport(passport):
            valid_passports += 1
    return valid_passports


def valid_passport(passport):
    if len(passport) != 7:
        return False
    if not(1920 <= int(passport["byr"]) <= 2002):
        return False
    if not(2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not(2020 <= int(passport["eyr"]) <= 2030):
        return False
    height_unit = re.match('(.+)(cm|in)', passport["hgt"])
    if height_unit is None or len(height_unit.groups()) != 2:
        return False
    height, unit = height_unit.groups()
    if unit == "cm" and (not (150 <= int(height) <= 193)):
        return False
    if unit == "in" and (not (59 <= int(height) <= 76)):
        return False
    hair_colour = re.match('(#[0-9a-f]{6}$)', passport["hcl"])
    if hair_colour is None:
        return False
    eye_colour = re.match('(amb|blu|brn|gry|grn|hzl|oth)$', passport["ecl"])
    if eye_colour is None:
        return False
    if len(passport["pid"]) != 9:
        return False
    return True


def parse_passport_data(lines):
    passports = []
    passport = dict()
    for line in lines:
        if line == "\n":
            passports.append(passport)
            passport = dict()
            continue
        for token in line.split(" "):
            token = token.strip()
            key, value = token.split(":")
            if key != "cid":
                passport[key] = value
    passports.append(passport)
    return passports


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(passport_check(lines)))