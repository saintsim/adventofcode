#!/usr/bin/env python3

import re

WAYS = 0
WAYS_A = []
VALID_CACHE = dict()
NOT_VALID_CACHE = dict()
COMBO_CACHE = dict()


def parse(input):
    patterns_input, towels_input = input.split('\n\n')
    patterns = [x.strip() for x in patterns_input.split(',')]
    towels = towels_input.split('\n')
    return patterns, towels


def update_cache(combos):
    for idx, item in enumerate(combos):
        key = ''.join(combos[idx:])
        if key in COMBO_CACHE:
            if combos[idx:] not in COMBO_CACHE[key]:
                COMBO_CACHE[key].append(combos[idx:])
        else:
            COMBO_CACHE[key] = [combos[idx:]]


def is_valid(towel, patterns, combos):
    global WAYS, WAYS_A
    if towel == '':
        WAYS += 1
        if combos not in WAYS_A:
            WAYS_A.append(combos)
        update_cache(combos)
        return True
    for pattern in patterns:
        if towel.startswith(pattern):
            new_combos = list(combos)
            tokens_left = re.sub(pattern, '', towel, 1)
            new_combos.append(pattern)

            if len(combos):
                update_cache(combos)

            if tokens_left in VALID_CACHE and tokens_left in COMBO_CACHE:
                WAYS += len(COMBO_CACHE[tokens_left])
                for c in COMBO_CACHE[tokens_left]:
                    if c not in WAYS_A:
                        WAYS_A.append(c)
            elif tokens_left in NOT_VALID_CACHE:
                continue
            else:
                print('checking: ' + str(tokens_left))
                valid = is_valid(tokens_left, patterns, list(new_combos))
                if valid:
                    VALID_CACHE[''.join(new_combos)] = True
                else:
                    NOT_VALID_CACHE[''.join(new_combos)] = True
    return False


def part1(input):
    global WAYS, WAYS_A, VALID_CACHE, NOT_VALID_CACHE
    total = 0
    patterns, towels = parse(input)
    for towel in towels:
        WAYS = 0
        WAYS_A = []
        is_valid(towel, patterns, [])
        total += WAYS
    return total


if __name__ == '__main__':
    with open('example', 'r') as file:
        print('Result: ' + str(part1(file.read())))

