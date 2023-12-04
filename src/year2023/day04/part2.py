#!/usr/bin/env python3

POINT_CARD_FORMULA = {}


def get_solution(card_num):
    values = POINT_CARD_FORMULA[int(card_num)]
    if not values:
        return []
    for val in values:
        if val.startswith('#'):
            return None
    return values


def brute_force():
    while True:
        solved = True
        for idx, row in POINT_CARD_FORMULA.items():
            # replace # with actual ones
            new_row = []
            for item in row:
                if item.startswith('#'):
                    solved = False
                    _, card_num = item.split('#')
                    solution = get_solution(card_num)
                    if solution is not None:
                        new_row.append(card_num)
                        for sol in solution:
                            new_row.append(sol)
                        continue
                new_row.append(item)
            POINT_CARD_FORMULA[idx] = new_row
        if solved:
            return


def compute_formulas(input):
    card_number = 1
    for line in input:
        _, tiles = line.split(":")
        wins, users = tiles.split(" | ")
        wins = wins.split()
        users = users.split()
        matches = 0
        for user in users:
            if user in wins:
                matches += 1
        if matches:
            # win points of cards below
            formulas = []
            for i in range(matches):
                formulas.append('#' + str((card_number + i + 1)))
            POINT_CARD_FORMULA[card_number] = formulas
        else:
            POINT_CARD_FORMULA[card_number] = []
        card_number += 1


def part2(input):
    total = 0
    compute_formulas(input)
    brute_force()
    for row in POINT_CARD_FORMULA.values():
        row_length = len(row) + 1
        print(row_length)
        total += row_length
    print("---")
    print(total)


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part2(file.read().split('\n'))))