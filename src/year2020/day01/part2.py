#!/usr/bin/env python3


def expense_report(lines):
    for line in lines:
        for other_line in lines:
            if line == other_line:
                continue
            for yet_another_line in lines:
                if (int(line) + int(other_line) + int(yet_another_line)) == 2020:
                    return str(int(line) * int(other_line) * int(yet_another_line))
    return ""


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(expense_report(lines)))
