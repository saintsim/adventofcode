#!/usr/bin/env python3

tokens = []


def token_parse(token):
    # ABCDE
    #  1002
    # DE - two-digit opcode
    # C - mode of 1st parameter
    # B - mode of 2nd parameter
    # A - mode of 3rd parameter
    # mode is either 0 for position mode (day02 default) or 1 for immediate mode
    a_mode = b_mode = c_mode = 0
    token_str = str(token)
    opcode = token_str[-2:]
    if len(token_str) > 2:
        c_mode = token_str[-3:-2]

    if len(token_str) > 3:  # e.g. 1002
       b_mode = token_str[-4:-3]

    if len(token_str) > 4:  # e.g. 11002
       c_mode = token_str[-5:-4]

    if len(token_str) > 5:
        raise ValueError(
            "token is longer than 5 chars, looks wrong")

    return int(a_mode), int(b_mode), int(c_mode), int(opcode)


def get_token(location, mode):
    try:
        # immediate mode
        if mode == 1:
            return int(location)
        else:
            # position mode
            global tokens
            return int(tokens[location])
    except:
        pass


def diagnostic_program(input, user_inputs):
    global tokens
    tokens = input
    # [99] means that the program is finished
    # [1] adds together numbers read from two positions and stores the result in a third position
    #     The three integers immediately after the opcode tell you these three positions -
    #     the first two indicate the positions from which you should read the input values,
    #     and the third indicates the position at which the output should be stored.
    # [2] works exactly like opcode [1], except it multiplies the two inputs instead of adding them.
    #     Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
    # [3] takes a single integer as input and saves it to the position given by its only parameter.
    #     For example, the instruction 3,50 would take an input value and store it at address 50.
    # [4] outputs the value of its only parameter. For example,
    #     the instruction 4,50 would output the value at address 50.
    # [5] is jump-if-true: if the first parameter is non-zero,
    #     it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # [6] is jump-if-false: if the first parameter is zero,
    #     it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # [7] is less than: if the first parameter is less than the second parameter,
    #     it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    # [8] is equals: if the first parameter is equal to the second parameter,
    #     it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    index = 0
    output = ''
    while True:
        element = tokens[index]
        # print('El -> ' + str(element))
        a_mode, b_mode, c_mode, opcode = token_parse(element)
        shift = 0
        if opcode == 99:
            return output
        elif opcode == 1:
            tokens[tokens[index+3]] = get_token(tokens[index+1], c_mode) + get_token(tokens[index+2], b_mode)
            shift = 4
        elif opcode == 2:
            tokens[tokens[index+3]] = get_token(tokens[index+1], c_mode) * get_token(tokens[index+2], b_mode)
            shift = 4
        elif opcode == 3:  # magic input number
            tokens[tokens[index+1]] = user_inputs.pop(0)
            shift = 2
        elif opcode == 4:
            to_print = get_token(tokens[index+1], c_mode)
            output = to_print
            shift = 2
        elif opcode == 5:
            first_param = get_token(tokens[index+1], c_mode)
            if first_param != 0:
                index = get_token(tokens[index+2], b_mode)
            else:
                shift = 3
        elif opcode == 6:
            first_param = get_token(tokens[index+1], c_mode)
            if first_param == 0:
                index = get_token(tokens[index+2], b_mode)
            else:
                shift = 3
        elif opcode == 7:
            first_param = get_token(tokens[index + 1], c_mode)
            second_param = get_token(tokens[index + 2], b_mode)
            tokens[tokens[index + 3]] = 1 if first_param < second_param else 0
            shift = 4
        elif opcode == 8:
            first_param = get_token(tokens[index + 1], c_mode)
            second_param = get_token(tokens[index + 2], b_mode)
            tokens[tokens[index + 3]] = 1 if first_param == second_param else 0
            shift = 4
        index += shift


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()[0]
        print('Result: ' + str(diagnostic_program(list(map(int, input.split(","))), [5])))
