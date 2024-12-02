#!/usr/bin/env python3

SAFE = 1
UNSAFE = 0


def safe_check(tokens, check_count):
    if tokens[1] > tokens[0]:
        # increasing
        for idx, line in enumerate(range(len(tokens) - 1)):
            if tokens[idx+1] > tokens[idx]:
                diff = tokens[idx+1] - tokens[idx]
                if diff < 1 or diff > 3:
                    # here
                    if check_count > 0:
                        return safe_check(tokens[:idx] + tokens[idx+1:], 0)
                    else:
                        return UNSAFE
            else:
                # safe
                if check_count > 0:
                    return safe_check(tokens[:idx] + tokens[idx + 1:], 0)
                else:
                    return UNSAFE
        return SAFE
    else:
        # decreasing
        for idx, line in enumerate(range(len(tokens)-1)):
            if tokens[idx] > tokens[idx+1]:
                diff = tokens[idx] - tokens[idx+1]
                if diff < 1 or diff > 3:
                    # safe
                    if check_count > 0:
                        return safe_check(tokens[:idx] + tokens[idx+1:], 0)
                    else:
                        return UNSAFE
            else:
                # safe
                if check_count > 0:
                    return safe_check(tokens[:idx] + tokens[idx + 1:], 0)
                else:
                    return UNSAFE
        return SAFE
    pass


def part2(input):
    safe_count = 0
    for line in input.split('\n'):
        if safe_check(list(map(int, line.split())), 1) == SAFE:
            safe_count += 1
    return safe_count


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))