#!/usr/bin/env python3

import random
import sys


intro = \
"""
A game consists of

   * 2 players;
   * 10 frames;
   * 2 bowls per frame.

The platform receives input in the form of a number between 1-10
The platform must determine the winner

Ready to start? Press enter:

"""


state = {'A':[], 'B':[], 'frame':0}


def choose_player():
    """
    Random choice of one of 2 players.
    Returns Bool
    """
    return(random.getrandbits(1))


def first_frame():
    """
    Random result for ball throw.
    Returns random integer between 0 and 10
    """
    return(random.randint(0,10))


def second_frame(score):
    """
    Random result for ball throw.
    Returns interger, but the probability of hitting a pin is lower.
    """
    return(random.randint(0, 10 - score))


def player_turn(player):
    """
    Player turn.
    Returns result of up to two frames.
    """
    input("Player {0}, Frame {1}. Press Enter to throw ball."\
              .format(player, state['frame']))
    score = first_frame()
    print("Score: {0}".format(score))

    if score < 10:
        input("Player {0}, Frame {1}. Press Enter to throw ball."\
              .format(player, state['frame']))
        score += second_frame(score)
    print("Score: {0}".format(score))
    return(score)


def game_loop():
    """
    Loops game alternating players
    until we reach 10 frames.
    Result is saved in global state (a side effect).
    """
    players = ['A','B']
    choice = choose_player()
    player_1 = players[choice]
    player_2 = players[not choice]
    while state['frame'] < 10:
        state[player_1].append(player_turn(player_1))
        state[player_2].append(player_turn(player_2))
        state['frame'] += 1
        print('-- A: {0} -- B: {1} --'.format(sum(state['A']),
                                                  sum(state['B'])))


def results():
    """
    Calculates results from global state and determines the winner.
    """
    A = sum(state['A'])
    B = sum(state['B'])
    print("Scores:\nA: {0}\nB: {1}".format(A,B))
    if A > B:
        print("A is the winner!")
    elif A < B:
        print("B is the winner!")
    else:
        print("It is a draw!")


def main(argv=None):
    if argv is None:
        argv = sys.argv

    input(intro)
    game_loop()
    results()


if __name__ == "__main__":
    main()
