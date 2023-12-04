#!/usr/bin/env python3

def part1(input):
    total = 0
    for line in input:
        _, tiles = line.split(":")
        wins, users = tiles.split(" | ")
        wins = wins.split()
        users = users.split()
        matches = 0
        for user in users:
            if user in wins:
                matches += 1
        if matches:
            points = pow(2, matches - 1)
            total += points
    print("---")
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read().split('\n'))))
