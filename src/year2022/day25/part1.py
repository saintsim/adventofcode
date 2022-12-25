#!/usr/bin/env python3


def snafu_digit_to_decimal(snafu_digit, idx):
    snafu_digit = snafu_digit.replace('-', '-1').replace('=', '-2')
    return int(snafu_digit) * pow(5,idx)


def snafu_to_decimal(term):
    return sum(snafu_digit_to_decimal(snafu_digit, idx) for idx, snafu_digit in enumerate(term [::-1]))


def base_five_to_snafu(digits):
    i = len(digits)-1
    #  (3, '1='),
    #  (4, '1-'),
    #  (5, '10'),
    while i >= 0:
        if digits[i] > 2:
            # prev digit + 1, set this to =
            if digits[i] == 3:
                digits[i] = '='
            elif digits[i] == 4:
                digits[i] = '-'
            else:  # 5
                digits[i] = 0
            if i < 1:
                digits = [1] + digits
            else:
                digits[i-1] += 1
        i -= 1
    return digits


def decimal_to_snafu(term):
    #       125 25 5 1
    # 1=-0-2  ->  1747
    digits = []
    overflow = False
    # standard base logic
    while term:
        digit_to_add = int(term % 5)
        if digit_to_add > 2:
            overflow = True
        digits.append(digit_to_add)
        term = int(term / 5)
    digits.reverse()
    # custom logic to cope with snafu not allowing terms more than 2
    if overflow:
        digits = base_five_to_snafu(digits)
    digits = [str(d) for d in digits]
    return ''.join(digits)


def snafu(lines):
    total = 0
    for line in lines:
        snafu_decimal = snafu_to_decimal(line)
        print(line, ' -> ', snafu_decimal)
        total += snafu_decimal
    print('Total: ', total)
    snarfu = decimal_to_snafu(total)
    snafu_decimal = snafu_to_decimal(snarfu)
    print('Snarfu: ' + snarfu, ', Snarfu validation: ', total == snafu_decimal)
    return snarfu


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        print(snafu(lines))
