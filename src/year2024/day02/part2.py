#!/usr/bin/env python3

SAFE = 1
UNSAFE = 0


def safe_check(tokens):
    if tokens[1] > tokens[0]:
        # increasing
        for idx in range(len(tokens) - 1):
            if tokens[idx+1] > tokens[idx]:
                diff = tokens[idx+1] - tokens[idx]
                if diff < 1 or diff > 3:
                    return UNSAFE
            else:
                return UNSAFE
        return SAFE
    else:
        # decreasing
        for idx in range(len(tokens)-1):
            if tokens[idx] > tokens[idx+1]:
                diff = tokens[idx] - tokens[idx+1]
                if diff < 1 or diff > 3:
                    return UNSAFE
            else:
                return UNSAFE
        return SAFE


def part2(input):
    safe_count = 0
    i = 0
    for line in input.split('\n'):
        line_list = list(map(int, line.split()))
        is_safe = False
        if safe_check(line_list) == SAFE:
            print(str(line_list))
            is_safe = True
        else:
            for idx in range(len(line_list)):
                new_list = list(line_list)
                del new_list[idx]
                if safe_check(new_list) == SAFE:
                    print(str(line_list))
                    is_safe = True
                    break
        if is_safe:
            safe_count += 1
        i += 1
    return safe_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
