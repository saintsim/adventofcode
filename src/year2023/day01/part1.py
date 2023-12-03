#!/usr/bin/env python3


def part1(input):
    total = 0
    for line in input.split():
        x = "foo"
        y = "bar"
        for c in line:
            if not c.isalpha():
                if x == "foo":
                    x = c
                else:
                    y = c
        if y == "bar":
            y = x
        res = int(x + y)
        print(res)
        total += res
    print("---")
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
