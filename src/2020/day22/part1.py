#!/usr/bin/env python3


def cards(file):
    cards = parse(file)
    while len(cards[0]) and len(cards[1]):
        player1_top = cards[0].pop(0)
        player2_top = cards[1].pop(0)
        cards[player1_top < player2_top] += [max(player1_top, player2_top), min(player1_top, player2_top)]
    winner = cards[0] if len(cards[0]) else cards[1]
    winner.reverse()
    return sum([winner_card * (idx+1) for idx, winner_card in enumerate(winner)])


def parse(file):
    cards = []
    for player in file.split('\n\n'):
        cards.append([int(item) for item in player.split(':')[1].split('\n') if len(item)])
    return cards


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(cards(file.read())))