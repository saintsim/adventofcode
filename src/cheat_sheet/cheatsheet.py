#!/usr/bin/env python3

from collections import Counter


def string_examples():
    name = 'Bob'
    print(name)
    upper_name = name.upper()
    print('Upper name: ', upper_name)
    lower_name = name.lower()
    print('Lower name: ', lower_name)
    length_of_name = len(name)
    print('Length of Name: ', length_of_name)
    freq_by_letters = Counter(name)
    print(freq_by_letters)


def lists():
    a = ['foo']


def switch():
    result = 'win'
    points = 0
    # python 3.10 feature- switch statements called match
    # match result:
    #     case 'win':
    #         points = 3


def loops():
    input = ['a', 'b', 'c']
    for idx, item in enumerate(input):
        print(idx, item) # prints 0 a etc.


if __name__ == '__main__':
    string_examples()
    loops()
