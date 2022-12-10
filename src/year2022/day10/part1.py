#!/usr/bin/env python3

signal_strengths = []


def cycle_update(i, register_x):
    print(i + 1, register_x, (i + 1) * register_x)
    signal_strengths.append((i + 1) * register_x)


def get_result(idxs):
    print([signal_strengths[i-1] for i in idxs])
    return sum(signal_strengths[i-1] for i in idxs)


def clock_circuit(input):
    instruction_index, register_x, number_of_cycles = 0, 1, 220
    to_add = None
    for i in range(number_of_cycles):
        cycle_update(i, register_x)
        if to_add is not None:
            register_x += int(to_add)
            to_add = None
        elif instruction_index < len(input):
            instruction = input[instruction_index].split()
            if instruction[0] != 'noop':
                to_add = instruction[-1]
                continue
        instruction_index += 1
    return get_result([20, 60, 100, 140, 180, 220])


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print('Result: ' + str(clock_circuit(lines)))
