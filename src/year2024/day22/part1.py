#!/usr/bin/env python3

import math


def parse(input):
    secret_numbers = []
    for secret in input.split('\n'):
        secret_numbers.append(int(secret))
    return secret_numbers


def mix_number(number, secret_number):
    return number ^ secret_number


def prune_number(number):
    return number % 16777216


def calc_next_secret_number(secret_number):
    next_secret_number = prune_number(mix_number(secret_number * 64, secret_number))
    next_secret_number_2 = prune_number(mix_number(math.floor(next_secret_number/32), next_secret_number))
    next_secret_number_3 = prune_number(mix_number(math.floor(next_secret_number_2*2048), next_secret_number_2))
    return next_secret_number_3


def part1(input):
    secret_numbers = parse(input)
    total = 0
    for secret_number in secret_numbers:
        next_secret_number = secret_number
        for _ in range(2000):
            next_secret_number = calc_next_secret_number(next_secret_number)
            print(next_secret_number)
        total += next_secret_number
    return total


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(part1(file.read())))
