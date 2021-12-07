#!/usr/bin/env python3

from collections import Counter


def calc_fuel_cost(from_amount, to_amount):
    smallest = min(from_amount, to_amount)
    largest = max(from_amount, to_amount)
    return sum(range((largest+1)-smallest))


def solve_fuel_amount(input):
    input_sorted = dict(Counter(input))
    least_fuel = float('inf')
    for fuel_cost in range(min(input), max(input)):
        total = 0
        for fuel_cost_2, freq_2 in input_sorted.items():
            cost = calc_fuel_cost(fuel_cost_2, fuel_cost)*freq_2
            total += cost
            print(str(fuel_cost) + " ; " + str(fuel_cost_2) + " -> " + str(fuel_cost) + " = " + str(cost))
        least_fuel = min(least_fuel, total)
        print( "--")
    return least_fuel


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(solve_fuel_amount(list(map(int, file.readlines()[0].split(","))))))