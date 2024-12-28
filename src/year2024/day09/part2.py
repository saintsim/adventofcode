#!/usr/bin/env python3

def parse(input):
    disk = []
    idx = 0
    for i in range(0, len(input), 2):
        for _ in range(int(input[i])):
            disk.append(str(idx))
        if i < len(input)-1:
            for _ in range(int(input[i+1])):
                disk.append('.')
        idx += 1
    return disk


def move_blocks(disk):
    idx = 0
    last_back_idx = len(disk)-1
    while True:
        if idx > len(disk)-1 or set(disk[idx:]) == {'.'}:
            return disk
        if disk[idx] == '.':
            # look fwd how many gaps do I have
            length = 1
            for trial_idx in range(idx+1, len(disk)):
                if disk[trial_idx] == '.':
                    length += 1
                else:
                    break
            # we now have length spots to fill
            for back_element in range(last_back_idx, -1, -1):
                last_back_idx -= 1
                if back_element > len(disk)-1:
                    continue
                if disk[back_element] != '.':
                    item_to_move = disk[back_element]
                    # a candidate, but how many do we have of this flavour, does it match length
                    back_length = 1
                    for next_back_element in range(last_back_idx, -1, -1):
                        if disk[next_back_element] == item_to_move:
                            back_length += 1
                        else:
                            break
                    if back_length > length:
                        # TODO: move back pointer further, otherwise we repeat

                        continue
                    for back_move_idx in range(back_length):
                        disk.pop(back_element-1)
                    for move_idx in range(back_length):
                        disk[idx+move_idx] = item_to_move
                    for _ in range(length-1):
                        idx += 1
                    break
        idx += 1


def calc_checksum(disk):
    total = 0
    for idx, element in enumerate(disk):
        if element != '.':
            total += int(element) * idx
    return total


def part2(input):
    disk = parse(input)
    disk = move_blocks(disk)
    return calc_checksum(disk)


if __name__ == '__main__':
    with open('example', 'r') as file:
        print('Result: ' + str(part2(file.read())))

