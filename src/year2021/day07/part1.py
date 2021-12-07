#!/usr/bin/env python3

from collections import Counter


def solve_fuel_amount(input):
    input_sorted = dict(Counter(input))
    least_fuel = float('inf')
    for fuel_cost in input_sorted.keys():
        total = 0
        for fuel_cost_2, freq_2 in input_sorted.items():
            total += abs(fuel_cost_2-fuel_cost)*freq_2
        least_fuel = min(least_fuel, total)
    return least_fuel


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(solve_fuel_amount(list(map(int, file.readlines()[0].split(","))))))