#!/usr/bin/env python3

def syntax_scoring(input):
    scores = []
    for line in input:
        total_score = 0
        print("processing line: " + line)
        pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
        complete_points = {")": 1, "]": 2, "}": 3, ">": 4}
        stack = []
        corrupted_line = False
        for char in line:
            if char in pairs:
                stack.append(char)
            else:
                end_expect = pairs[stack.pop()]
                if char is not end_expect:
                    corrupted_line = True
                    break
        if corrupted_line is False:
            while len(stack) > 0:
                popped = stack.pop()
                total_score = (total_score * 5) + complete_points[pairs[popped]]
            print("Score = " + str(total_score))
            scores.append(total_score)
    scores.sort()
    return scores[int((len(scores)-1)/2)]


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(syntax_scoring(lines)))
