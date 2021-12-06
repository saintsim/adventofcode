#!/usr/bin/env python3


def solve_laternfish(fishes):
    print("initial: " + str(fishes))
    for day in range(80):
        new_fish = []
        for fish in fishes:
            if fish == 0:
                new_fish.append(6)
                new_fish.append(8) # new one
            else:
                new_fish.append(fish-1)
            fishes = new_fish
        print("After " + str(day+1) + " day (" + str(len(fishes)) + ")")
        # + str(fishes) + " (" + str(len(fishes)) + ")")
    return len(fishes)


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        print('Result: ' + str(solve_laternfish(input)))
