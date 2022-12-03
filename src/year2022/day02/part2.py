#!/usr/bin/env python3


def calc_score(player1, player2, equivalent_action):
    #   Rock = 1    Opp = A,  Me = X
    #   Paper = 2   Opp = B   Me = Y
    #   Scissors = 3 Opp = C  Me = Z
    #   0 for L, 3 for D, 6 for W
    score_matrix = dict()
    score_matrix['X'] = 1
    score_matrix['Y'] = 2
    score_matrix['Z'] = 3
    round_score = score_matrix[player2]
    if player1 == equivalent_action[player2]:
        round_score += 3
    elif (player2 == 'X' and player1 == 'C') or (player2 == 'Y' and player1 == 'A') or (
            player2 == 'Z' and player1 == 'B'):
        round_score += 6
    print(round_score)
    return round_score


def rock_paper_scissors(input):
    score = 0
    equivalent_action = dict()
    equivalent_action['X'] = 'A'
    equivalent_action['Y'] = 'B'
    equivalent_action['Z'] = 'C'
    equivalent_action['A'] = 'X'
    equivalent_action['B'] = 'Y'
    equivalent_action['C'] = 'Z'

    for line in input:
        player1, player2 = line.strip().split()
        if player2 == 'X':
            # lose
            if player1 == 'A':
                player2 = 'Z'
            elif player1 == 'B':
                player2 = 'X'
            else:
                player2 = 'Y'
        elif player2 == 'Y':
            # draw
            player2 = equivalent_action[player1]
        else:
            # win
            if player1 == 'A':
                player2 = 'Y'
            elif player1 == 'B':
                player2 = 'Z'
            else:
                player2 = 'X'
        score += calc_score(player1, player2, equivalent_action)
    return score


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(rock_paper_scissors(file.readlines())))
