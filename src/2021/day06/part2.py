#!/usr/bin/env python3

def add_to_map(fish_map, fish, incr):
    if fish not in fish_map:
        fish_map[fish] = incr
    else:
        fish_map[fish] += incr
    return fish_map


def solve_lanternfish(fishes):
    # re-write of part 1 to use a map to make it more efficient
    print("initial: " + str(fishes))
    fish_map = {}
    for fish in fishes:
        add_to_map(fish_map, fish, 1)

    for day in range(256):
        new_fish = {}
        for fish, count in fish_map.items():
            if fish == 0:
                add_to_map(new_fish, 6, count)
                add_to_map(new_fish, 8, count)
            else:
                add_to_map(new_fish, fish-1, count)
            fish_map = new_fish
        print("After " + str(day+1))
    return sum(fish_map.values())


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        print('Result: ' + str(solve_lanternfish(input)))
