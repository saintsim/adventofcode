#!/usr/bin/env python3

import math


def parse(input):
    page_order_in, page_numbers_in = input.split('\n\n')
    page_order_rules = [list(map(int, p.split('|'))) for p in page_order_in.split('\n')]
    page_numbers = [list(map(int, p.split(','))) for p in page_numbers_in.split('\n')]
    return page_order_rules, page_numbers


def is_correctly_ordered(page_update, page_order_rules):
    for rule in page_order_rules:
        if rule[0] in page_update and rule[1] in page_update:
            if page_update.index(rule[0]) > page_update.index(rule[1]):
                print('wrong: ' + str(rule[0]) + ', before: ' + str(rule[1]))
                return False
    return True


def fix_order(page_update, page_order_rules):
    for rule in page_order_rules:
        if rule[0] in page_update and rule[1] in page_update:
            rule_zero_idx = page_update.index(rule[0])
            rule_one_idx = page_update.index(rule[1])
            if rule_zero_idx > rule_one_idx:
                page_update[rule_one_idx] = rule[0]
                page_update[rule_zero_idx] = rule[1]
    is_now_correct = is_correctly_ordered(page_update, page_order_rules)
    if is_now_correct:
        return page_update
    else:
        page_update = fix_order(page_update, page_order_rules)
    return page_update


def part2(input):
    total = 0
    page_order_rules, page_numbers = parse(input)
    for page_update in page_numbers:
        correctly_ordered = is_correctly_ordered(page_update, page_order_rules)
        if not correctly_ordered:
            # need to switch
            correct_order = fix_order(page_update, page_order_rules)
            total += correct_order[math.floor(len(correct_order)/2)]
        print(str(page_update) + ', -> ' + str(correctly_ordered))
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))

