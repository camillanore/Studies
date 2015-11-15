# -*- coding: utf-8 -*-
# Problem 8.14
# Author: Camilla Nore
# Date: 2015-11-05
"""
8.14 (freq_2dice.py, side 509)
 
Exercise 8.14: Compute probabilities of throwing two dice
Throw two dice a large number of times in a program. Record the sum of the eyes each time and count how many times each of the possibilities for the sum (2, 3, . . ., 12) appear. Compute the corresponding probabilities and compare them with the exact values. (To find the exact probabilities, set up all the 6 × 6 possible outcomes of throwing two dice, and then count how many of them that has a sum s for s = 2, 3, . . . , 12.) Filename: freq_2dice.py.
"""

import numpy as np
import random
import sys

def main():
    try:
        n_experiments = int(sys.argv[1])
    except:
        n_experiments = 1000

    print "Possible sums of two die:"
    combination_sums = np.zeros((6,6))
    for i in range(6):
        for j in range(6):
           combination_sums[i,j] = i+j+2 
    print combination_sums 

    empirical_results = np.asarray([eyes_sum(2) for i in range(n_experiments)])

    n_possible_sums = 11
    P_of_sum_monte = np.zeros(n_possible_sums)
    P_of_sum_exact = np.zeros(n_possible_sums)

    
    print '\nSum\tExact P(s)\tMonte Carlo'
    for i in range(n_possible_sums):
        P_of_sum_monte[i] = np.sum(empirical_results == i+1)*1.0/n_experiments
        P_of_sum_exact[i] = np.sum(combination_sums == i+1)/36.0
        print '%d\t%f\t%f'%(i+1, P_of_sum_exact[i], P_of_sum_monte[i])


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
    >python freq_2dice.py 10.4166666667 1000
    Possible sums of two die:
    [[  2.   3.   4.   5.   6.   7.]
     [  3.   4.   5.   6.   7.   8.]
     [  4.   5.   6.   7.   8.   9.]
     [  5.   6.   7.   8.   9.  10.]
     [  6.   7.   8.   9.  10.  11.]
     [  7.   8.   9.  10.  11.  12.]]

    Sum     Exact P(s)      Monte Carlo
    1       0.000000        0.000000
    2       0.027778        0.030000
    3       0.055556        0.055000
    4       0.083333        0.081000
    5       0.111111        0.112000
    6       0.138889        0.153000
    7       0.166667        0.172000
    8       0.138889        0.140000
    9       0.111111        0.099000
    10      0.083333        0.084000
    11      0.055556        0.042000
"""
