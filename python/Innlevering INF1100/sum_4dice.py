# Problem 8.8
# Author: Camilla Nore
# Date: 2015-11-05
# -*- coding: utf-8 -*-
"""
8.8 (sum_4dice.py, side 507), 
Exercise 8.8: Decide if a dice game is fair
 Somebody suggests the following game. You pay 1 euro and are allowed to throw four dice. If the sum of the eyes on the dice is less than 9, you get paid r euros back, otherwise you lose the 1 euro investment. Assume r = 10. Will you then in the long run win or lose money by playing this game? Answer the question by making a program that simulates the game. Read r and the number of experiments N from the command line. Filename: sum_4dice.py.
"""

import numpy as np
import random
import sys

def main():
    try:
        r = float(sys.argv[1])
        n_experiments = int(sys.argv[2])
    except:
        print 'Usage: argv[0] r n_experiments'
        sys.exit(1)
    n_throws = 4
    max_number_of_eyes = 9
    cost_of_one_game = 1.0 # Euro
    n_break_even = r / cost_of_one_game  # Win within n games to break even.

    results = [eyes_sum(n_throws) for i in range(n_experiments)]
    success = np.asarray(results) < max_number_of_eyes
    P = np.sum(success)*1.0/n_experiments
    P_break_even = P*n_break_even
    # Probability of winning in n
    print 'Monte-Carlo probability of winning one game: %f)'%(P)
    print 'Probability of break-even: %f)'%(P_break_even)
    if P_break_even > 0.5:
        print 'You should play this game.'
    else:
        print 'You should not play this game.'
 

def eyes_sum(N):
    """ Throw n dice, and return number of eyes. """
    eyes = np.random.randint(1, 7, N)
    M = np.sum(eyes)
    return M
 
 
if __name__ == '__main__':
    main()

""" Output:
    >python sum_4dice.py 10 1000
    Monte-Carlo probability of winning one game: 0.049000)
    Probability of break-even: 0.490000)
    You should not play this game.
"""
