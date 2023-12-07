#!/usr/bin/env python3

from collections import Counter
import functools

HANDS = {
    'HighCard': 1,
    '1Pair': 1,
    '2Pair': 1,
    '3Kind': 1,
    'FullHouse': 1,
    '4kind': 1,
    '5kind': 1
}

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def non_joker_count_req(cards, count_needed):
    for key, count in Counter(cards).items():
        if key != 'J' and count_needed == count:
            return True
    return False


def get_card_type(cards):
    counter_length = len(Counter(cards))
    joker_count = Counter(cards)['J']

    if counter_length == 1:
        return '5kind'

    if joker_count > 0:
        if counter_length == 2:
            return '5kind'
        if counter_length == 3 and non_joker_count_req(cards, 1):
            return '4kind'
        if counter_length == 3:
            return 'FullHouse'
        if counter_length == 4 and 2 in list(Counter(cards).values()):
            return '3Kind'
        if counter_length == 4:
            return '2Pair'
        return '1Pair'
    else:
        if counter_length == 1:
            return '5kind'
        if counter_length == 2 and (list(Counter(cards).values()) == [4, 1] or list(Counter(cards).values()) == [1, 4]):
            return '4kind'
        if counter_length == 2 and (list(Counter(cards).values()) == [3, 2] or list(Counter(cards).values()) == [2, 3]):
            return 'FullHouse'
        if 3 in list(Counter(cards).values()):
            return '3Kind'
        if counter_length == 3 and 2 in list(Counter(cards).values()) and 1 in list(Counter(cards).values()):
            return '2Pair'
        if 2 in list(Counter(cards).values()):
            return '1Pair'
        return 'HighCard'


def get_position(card):
    return order.index(card)


def compare(pair1, pair2):
    for idx in range(5):
        if get_position(pair1[0][idx]) < get_position(pair2[0][idx]):
            return 1
        if get_position(pair1[0][idx]) > get_position(pair2[0][idx]):
            return -1
    # must be the same
    return 0


def rank_pairs(pairs):
    return sorted(pairs, key=functools.cmp_to_key(compare))


def calc_score(all_cards):
    rank = 1
    total = 0
    for hand in HANDS:
        if hand in all_cards:
            for cards in all_cards[hand]:
                bid = int(cards[1])
                total += (bid * rank)
                print(cards[0], bid, rank)
                rank += 1
    return total


def part2(input):
    card_by_type = {}
    for line in input.split('\n'):
        cards, score = line.split()
        type = get_card_type(cards)
        if type not in card_by_type:
            card_by_type[type] = [(cards, score)]
        else:
            card_by_type[type].append((cards, score))
    for type, pairs in card_by_type.items():
        if len(pairs) > 1:
            ranked_pairs = rank_pairs(pairs)
            card_by_type[type] = ranked_pairs
    return calc_score(card_by_type)


if __name__ == '__main__':
    with open('input', 'r') as file:
         print('Result: ' + str(part2(file.read())))
