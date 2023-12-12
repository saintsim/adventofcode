#!/usr/bin/env python3

from collections import Counter
from itertools import permutations


def easy_case(spring_map, damaged_map):
    case_total = 0
    for idx in range(len(spring_map)):
        damage_expected = int(damaged_map[idx])
        count = Counter(spring_map[idx])
        current_hash_count = count['#']
        current_question_count = count['?']
        if (current_hash_count == damage_expected) or damage_expected == (current_hash_count + current_question_count):
            # nothing to do
            continue
        else:
            new_springs = (damage_expected * ['#']) + (len(spring_map[idx])-damage_expected) * ['?']
            res = len(set(permutations(new_springs)))
            case_total += res
    return 1 if case_total == 0 else case_total


def part1(input):
    total = 0
    for line in input.split('\n'):
        springs, damaged_count = line.split()
        spring_map = []
        if '?' not in springs:
            print(line, " -> ", 1)
            total += 1
            continue
        for spring in springs.split('.'):
            if len(spring):
                spring_map.append(spring)
        damaged_map = damaged_count.split(',')
        if len(damaged_map) == len(spring_map):
            sub_total = easy_case(spring_map, damaged_map)
            total += sub_total
            print(line, " -> ", sub_total)
        else:
            # panic
            print(line, " -> ??")
    return total


# operational (.) or damaged (#), or unknown (?)  - number of damaged
# ->>  #.#.### 1,1,3  means 1 was damaged, another 1 was damaged, and then 3 were damaged


if __name__ == '__main__':
    with open('example', 'r') as file:
        print('Result: ' + str(part1(file.read())))