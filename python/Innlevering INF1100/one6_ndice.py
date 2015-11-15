# Problem 8.6
# Author: Camilla Nore
# Date: 2015-11-05
# -*- coding: utf-8 -*-

"""
Exercise 8.6: Estimate the probability in a dice game
Make a program for estimating the probability of getting at least one die with 
six eyes when throwing n dice. Read n and the number of experiments from the 
command line. As a partial verification, compare the Monte Carlo simulation 
results to the exact answer 11/36 for n = 2 and observe that the approximate 
probabilities approach the exact probability as the number of simulations grow. 
Filename: one6_ndice.py
"""
import numpy as np
import random
import sys

def main():
    try:
        n_throws = int(sys.argv[1])
        n_experiments = int(sys.argv[2])
    except:
        print 'Usage: argv[0] n_throws n_experiments'
        sys.exit(1)
    results = [six_eyes_vec(n_throws) for i in range(n_experiments)]
    number_of_six = np.asarray(results) > 0
    P = np.sum(number_of_six)*1.0/n_experiments
    print 'Monte-Carlo result: %f, exact solution: %f)'%(P, 11/36.0)
 

def six_eyes_vec(N):
    """ Throw n dice, and return number of sixes. """
    eyes = np.random.randint(1, 7, N)
    success = eyes == 6     # True/False array
    M = np.sum(success)     # treats True as 1, False as 0
    return float(M)/N
 
 
if __name__ == '__main__':
    main()


""" Output:
    :!python one6_ndice.py 2 1000
    Monte-Carlo result: 0.335000, exact solution: 0.305556)
"""
