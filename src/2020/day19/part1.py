#!/usr/bin/env python3

import re

RULES = dict()
MESSAGES = []


class Rule:
    def __init__(self, encoded_rule):
        self.encoded_rule = encoded_rule
        self.rule_already_decoded = False
        self.decoded_rule = ''

    def set_decoded_rule(self, decoded_rule):
        self.decoded_rule = decoded_rule
        all_done = True
        for i in decoded_rule:
            if str(i).isnumeric():
                all_done = False
        self.rule_already_decoded = all_done


def rule_checker(lines, max_depth):
    parse(lines)
    decode_rule(0, 0, max_depth)
    return find_matches()


def find_matches():
    matches = [re.fullmatch(RULES[0].decoded_rule, message) for message in MESSAGES]
    return len([match for match in matches if match is not None])


def decode_rule(i, depth, max_depth):
    # clearly a hack but helps get us part 2
    if max_depth != 'no max' and depth > max_depth:
        return ''
    if RULES[i].rule_already_decoded:
        return RULES[i].decoded_rule
    decoded_elements = '('
    for element in RULES[i].encoded_rule.split():
        if str(element).isnumeric():
            decoded_elements += decode_rule(int(element), depth+1, max_depth)
        else:
            decoded_elements += element.strip('"')
    decoded_elements += ')'
    RULES[i].decoded_rule = decoded_elements
    return decoded_elements


def parse(lines):
    for line in lines:
        if ':' in line:
            index, rule = line.split(':')
            RULES[int(index)] = Rule(rule.strip())
        elif line != '':
            MESSAGES.append(line)
    return MESSAGES


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(rule_checker(lines, 'no max')))
