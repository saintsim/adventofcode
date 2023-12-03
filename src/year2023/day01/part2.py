#!/usr/bin/env python3

NUMS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def part2(input):
    total = 0
    for line in input.split():
        first_num_idx = 999
        first_num = 999
        last_num_idx = -1
        last_num = -1
        for key in NUMS:
            idx = line.find(key)
            if idx != -1:
                if idx < first_num_idx:
                    first_num_idx = idx
                    first_num = NUMS[key]
            r_idx = line.rfind(key)
            if r_idx != -1:
                if r_idx > last_num_idx:
                    last_num_idx = r_idx
                    last_num = NUMS[key]
        res = int(str(first_num) + str(last_num))
        print(res)
        total += res
    print('----')
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read())))
