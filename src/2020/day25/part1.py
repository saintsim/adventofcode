#!/usr/bin/env python3


def encryption_key(file):
    key1, key2 = parse(file)
    # loop_size1 = compute_loop_size(7, key1)
    loop_size2 = compute_loop_size(7, key2)
    return compute_key(key1, loop_size2)


def compute_loop_size(subject_number, target):
    current_value, loop_size = 1, 0
    while current_value != target:
        current_value = (current_value * subject_number) % 20201227
        loop_size += 1
    return loop_size


def compute_key(subject_number, target_loop_size):
    current_value = 1
    for _ in range(target_loop_size):
        current_value = (current_value * subject_number) % 20201227
    return current_value


def parse(file):
    return list(map(int, file.split('\n')))


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(encryption_key(file.read())))