#!/usr/bin/env python3

def part1(input):
    invalid_id_count = 0
    for pid in input.split(","):
        id_from, id_to = pid.split("-")
        id_range = range(int(id_from), int(id_to)+1)
        for id_to_check in id_range:
            if is_id_invalid(id_to_check):
                invalid_id_count += id_to_check
    return invalid_id_count


def is_id_invalid(pid):
    id_list = list(str(pid))
    if len(id_list) % 2 != 0:
        return False
    middle_point = len(id_list) // 2
    if id_list[:middle_point] == id_list[middle_point:]:
        return True
    return False


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
