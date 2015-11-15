# Problem 8.9
# Author: Camilla Nore
# Date: 2015-11-05
# -*- coding: utf-8 -*-
"""
Exercise 8.9: Adjust a game to make it fair
It turns out that the game in Exercise 8.8 is not fair, since you lose money in the long run. The purpose of this exercise is to adjust the winning award so that the game becomes fair, i.e., that you neither lose nor win money in the long run. Make a program that computes the probability p of getting a sum less than s when rolling n dice. Use the reasoning in Section 8.3.2 to find the award per game, r, that makes the game fair. Run the program from Exercise 8.8 with this r on the command line and verify that the game is now fair. Filename: sum_s_ndice_fair.py.
"""

import numpy as np
import random
import sys

def main():
    try:
        r = int(sys.argv[1])
        n_experiments = int(sys.argv[2])
    except:
        print 'Usage: argv[0] r n_experiments'
        print sys.argv
        r = 10
        n_experiments = 100
    n_throws = 4
    max_number_of_eyes = 9
    cost_of_one_game = 1.0 # Euro
    n_break_even = r / cost_of_one_game  # Win within n games to break even.
    results = [eyes_sum(n_throws) for i in range(n_experiments)]
    success = np.asarray(results) < max_number_of_eyes
    P = P_sum_less_than(max_number_of_eyes, n_throws, n_experiments)
    fair_return = 0.5/P
    # Probability of winning in n
    print 'Monte-Carlo probability of winning one game: %f)'%(P)
    print 'Fair return:', fair_return


def P_sum_less_than( max_eyes, n_throws, n_experiments):
    results = [eyes_sum(n_throws) for i in range(n_experiments)]
    success = np.asarray(results) < max_eyes
    P = np.sum(success)*1.0/n_experiments
    return P


def eyes_sum(N):
    """ Throw n dice, and return number of eyes. """
    eyes = np.random.randint(1, 7, N)
    M = np.sum(eyes)     # treats True as 1, False as 0
    return M
 
 
if __name__ == '__main__':
    main()

""" Output:
    >python sum_s_ndice_fair.py 10 1000
    Monte-Carlo probability of winning one game: 0.048000)
    Fair return: 10.4166666667

    Verification by running:
    >python sum_4dice.py 10.4166666667 1000
    Monte-Carlo probability of winning one game: 0.056000)
    Probability of break-even: 0.583333)
    You should play this game.

    Comment:
    N = 1000 is too small to get reliable results for this.

"""
