#!/usr/bin/env python3


def shuttle_bus(lines):
    # 0 = every bus departed from the sea port
    # num is how often it leaves for the airport
    depart_time = int(lines[0])
    buses = lines[1].split(',')
    i = depart_time
    while True:
        for bus in buses:
            if bus != 'x':
                if i % int(bus) == 0:
                    res = int(bus) * (i-depart_time)
                    return res
        i += 1


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(shuttle_bus(lines)))
