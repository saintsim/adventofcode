#!/usr/bin/env python3

CUPS = []


def get_cup_idx(x):
    return x % len(CUPS)


def get_picked_up_cups(current_cup_idx):
    return [CUPS[get_cup_idx(current_cup_idx + y)] for y in range(1, 4)]


def get_other_cups(current, picked_up):
    return [cup for cup in CUPS if cup != current and cup not in picked_up]


def get_destination_cup(current_cup, picked_up_cups, other_cups):
    desired_number = current_cup-1
    while desired_number in picked_up_cups:
        desired_number -= 1
    return desired_number if desired_number > 0 else max(other_cups)


def get_output():
    return ''.join([str(CUPS[get_cup_idx(CUPS.index(1) + i)]) for i in range(1, len(CUPS))])


def cups(file):
    global CUPS
    CUPS = parse(file)
    current_cup_idx = 0
    for i in range(100):
        print('-- move {0} --\n{1}'.format(i+1, CUPS))
        # get the parts
        current_cup = CUPS[current_cup_idx]
        picked_up_cups = get_picked_up_cups(current_cup_idx)
        other_cups = get_other_cups(current_cup, picked_up_cups)
        destination_cup = get_destination_cup(current_cup, picked_up_cups, other_cups)
        print('Current cup: {0}'.format(current_cup))
        print('Picked up: {0}'.format(picked_up_cups))
        print('Destination: {0}'.format(destination_cup))
        # remove the picked up cups
        new_cups = [cup for cup in CUPS if cup not in picked_up_cups]
        # add them back in after the destination cup
        destination_cup_idx = new_cups.index(destination_cup)
        for y in range(1, 4):
            new_cups.insert(destination_cup_idx + y, picked_up_cups[y-1])
        CUPS = new_cups
        current_cup_idx = get_cup_idx(CUPS.index(current_cup)+1)
    print('-- final --\n{0}'.format(CUPS))
    return get_output()


def parse(file):
    return list(map(int, file))


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(cups(file.read())))