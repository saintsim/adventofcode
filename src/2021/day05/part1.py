#!/usr/bin/env python3

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(play_game()))