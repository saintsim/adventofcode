#!/usr/bin/env python3

signal_strengths = []
crt = []
current_line = []


def cycle_update(i, register_x):
    global current_line
    print(i + 1, register_x, (i + 1) * register_x)
    signal_strengths.append((i + 1) * register_x)
    if len(current_line) == 40:
        crt.append(current_line)
        current_line = []
    current_line.append('#' if i % 40 in (register_x-1, register_x, register_x+1) else '.')
    for line in crt:
        print(''.join(line))
    print(''.join(current_line))


def clock_circuit(input):
    instruction_index, register_x, number_of_cycles = 0, 1, 220
    to_add = None
    i = 0
    while len(crt) < 6:
        cycle_update(i, register_x)
        if to_add is not None:
            register_x += int(to_add)
            to_add = None
        elif instruction_index < len(input):
            instruction = input[instruction_index].split()
            if instruction[0] != 'noop':
                to_add = instruction[-1]
                i += 1
                continue
        instruction_index += 1
        i += 1
    return


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(clock_circuit(lines)))
