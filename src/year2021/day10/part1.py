#!/usr/bin/env python3

def syntax_scoring(input):
    bad_score = 0
    for line in input:
        print("processing line: " + line)
        bad_score_by_char = {")": 3, "]": 57, "}": 1197, ">": 25137}
        pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
        stack = []
        for char in line:
            if char in pairs:
                stack.append(char)
            else:
                end_expect = pairs[stack.pop()]
                if char is not end_expect:
                    bad_score += bad_score_by_char[char]
    return bad_score


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(syntax_scoring(lines)))
