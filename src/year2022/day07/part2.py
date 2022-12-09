#!/usr/bin/env python3

from part1 import linux, DIRECTORY_PTRS


def folder_to_delete(input):
    linux(input)
    update_size = 70000000
    free_space_needed = 30000000
    max_size = update_size - free_space_needed
    current_disk_usage = DIRECTORY_PTRS.get('/').dir_size
    to_clear = current_disk_usage - max_size
    print('to clear =>', current_disk_usage - max_size)
    option = free_space_needed
    for dir_idx in DIRECTORY_PTRS.values():
        if to_clear <= dir_idx.dir_size < option:
            option = dir_idx.dir_size
    return option


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(folder_to_delete(file.read())))