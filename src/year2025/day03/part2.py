#!/usr/bin/env python3

def part1(input):
    total = 0
    for line in input.split("\n"):
        largest_num = ''
        batteries = list(map(int, line))
        print("-> ", line)
        for gap in range(12, 0, -1):
            # print("gap -> ", gap)
            if gap == 1:
                largest = max(batteries)
            else:
                largest = max(batteries[:(-1*(gap-1))])
            # print("largest -> ", largest)
            largest_num += str(largest)
            largest_loc = batteries.index(largest)
            batteries = batteries[largest_loc+1:]
        print('= ' + largest_num)
        print('---')
        total += int(largest_num)
    print("====")
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
