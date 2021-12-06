#!/usr/bin/env python3

CUPS = dict()
CURRENT = []
TOP_FIVE = set()


def get_picked_up_cups():
    picked_up_one = CUPS[CURRENT[0]]
    picked_up_two = CUPS[picked_up_one]
    picked_up_three = CUPS[picked_up_two]
    return [picked_up_one, picked_up_two, picked_up_three]


def get_destination_cup(current_cup, picked_up_cups):
    desired_number = current_cup-1
    while desired_number in picked_up_cups:
        desired_number -= 1
    picked_up_cups_set = set(picked_up_cups)
    return desired_number if desired_number > 0 else max(TOP_FIVE - picked_up_cups_set)


def get_output():
    cup_a = CUPS[1]
    cup_b = CUPS[cup_a]
    return cup_a * cup_b


def cups(file):
    parse(file)
    for i in range(10000000):
        # print('-- move {0} --\n{1}'.format(i+1, CUPS))
        # get the parts
        current_cup = CURRENT[0]
        picked_up_cups = get_picked_up_cups()
        destination_cup = get_destination_cup(current_cup, picked_up_cups)
        # print('Current cup: {0}'.format(current_cup))
        # print('Picked up: {0}'.format(picked_up_cups))
        # print('Destination: {0}'.format(destination_cup))
        # move the picked up cups to after the destination cup
        picked_up_cups_end_pt = CUPS[picked_up_cups[2]]
        current_destination_pt = CUPS[destination_cup]
        CUPS[destination_cup] = picked_up_cups[0]
        CUPS[picked_up_cups[2]] = current_destination_pt
        CUPS[current_cup] = picked_up_cups_end_pt
        CURRENT[0] = CUPS[current_cup]
    # print('-- final --\n{0}'.format(CUPS))
    return get_output()


def parse(file):
    base_list = list(map(int, file))
    full_list = base_list + list(range(len(base_list) + 1, 1000001))
    for i, item in enumerate(full_list):
        if i == len(full_list)-1:
            CUPS[item] = full_list[0]
        else:
            CUPS[item] = full_list[i+1]
    CURRENT.append(full_list[0])
    global TOP_FIVE
    TOP_FIVE = set(full_list[-5:])


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(cups(file.read())))
