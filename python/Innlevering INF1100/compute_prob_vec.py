# Problem 8.2
# Author: Camilla Nore
# Date: 2015-11-05
# -*- coding: utf-8 -*-

import numpy as np
import random
import time


def compute_prob_vec(N=10, min_x=0.5, max_x=0.6):
    """ Find the probability empirically, by vector arithmetic. """
    r = np.asarray([random.uniform(0, 1) for i in range(N)])
    r1 = r[r > min_x]
    r2 = r1[r1 < max_x]
    return np.size(r2)*1.0/N


def compute_prob(N=10, min_x=0.5, max_x=0.6):
    """ Find the probability empirically. """
    y = [random.uniform(0, 1) for i in range(N)]
    M = 0.0
    for x in y:
        if x > min_x and x < max_x:
            M += 1
    return M/N


if __name__ == '__main__':
    """ Compute P both with vector method and with for loop, for different 
    values of N. Print the results and also the execution time of the two
    methods. """
    i = np.asarray([1, 2, 3, 6])
    print 'N,\tP_loop,\t\tP_vec,\t\tt_loop,\t\tt_vec'
    for j in i:
        N = 10**j
        t0 = time.time()
        P_vec = compute_prob_vec(N)
        t1 = time.time()
        P_loop = compute_prob(N)
        t2 = time.time()
        t_vec = t1 - t0
        t_loop = t2 - t1
        print '10e%d\t%f\t%f\t%f\t%f'%(j, P_loop, P_vec, t_loop, t_vec)

""" Ouput:
    :!python compute_prob_vec.py
    N,      P_loop,         P_vec,          t_loop,         t_vec
    10e1    0.000000        0.200000        0.000048        0.000366
    10e2    0.130000        0.130000        0.000255        0.000385
    10e3    0.077000        0.090000        0.002700        0.002963
    10e6    0.100272        0.100218        2.764008        3.009470
"""

