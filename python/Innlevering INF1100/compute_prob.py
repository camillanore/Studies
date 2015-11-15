# Problem 8.2
# Author: Camilla Nore
# Date: 2015-11-05
# -*- coding: utf-8 -*-

import random
import numpy as np

def compute_prob(N=10, min_x=0.5, max_x=0.6):
    """ Find the probability empirically. """
    y = [random.uniform(0,1) for i in range(N)]
    M = 0.0
    for x in y:
        if x > min_x and x < max_x:
            M += 1
    return M/N


if __name__ == '__main__':
    i = np.asarray([1, 2, 3, 6])
    for j in i:
        N = 10**j
        P = compute_prob(N)
        print 'P(x in (0.5,0.6) ) for N=10e%d is %f' %(j, P)

""" Ouput:
    :!python compute_prob.py
    P(x in (0.5,0.6) ) for N=10e1 is 0.000000
    P(x in (0.5,0.6) ) for N=10e2 is 0.090000
    P(x in (0.5,0.6) ) for N=10e3 is 0.106000
    P(x in (0.5,0.6) ) for N=10e6 is 0.100000
"""
