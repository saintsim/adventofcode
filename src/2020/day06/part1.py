#!/usr/bin/env python3


def customs_form_sum(lines):
    total, group = 0, set()
    for line in lines:
        if line == "\n":
            total += len(group)
            group = set()
        else:
            for token in line.strip():
                group.add(token)
    return total + len(group)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(customs_form_sum(file.readlines())))
