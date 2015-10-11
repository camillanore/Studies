# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:26:48 2015

@author: NBCNO1
"""

"""
Week 

Exercise 5.30: Plot Taylor polynomial approximations to sin x

The sine function can be approximated by a polynomial according to the
following formula:
sin x ≈ S(x; n) = sum over from j j=0 (−1)j /x2j+1 )/(2j + 1)! . (5.26)

The expression (2j + 1)! is the factorial (math.factorial can compute
this quantity). The error in the approximation S(x; n) decreases as n
increases and in the limit we have that limn→∞ S(x; n) = sin x. 
The purpose of this exercise is to visualize the quality of various approximations
S(x; n) as n increases.

a) Write a Python function S(x, n) that computes S(x; n). Use a
straightforward approach where you compute each term as it stands
in the formula, i.e., (−1)jx2j+1 divided by the factorial (2j + 1)!. (We
remark that Exercise A.14 outlines a much more efficient computation
of the terms in the series.)

b) Plot sin x on [0, 4π] together with the approximations S(x; 1), S(x; 2),
S(x; 3), S(x; 6), and S(x; 12).
Filename: plot_Taylor_sin.py.

"""
import math
import matplotlib.pyplot as plt

def terms(ti,x_0, N):
    i = 0
    t_list = []
    # for elements in array
    for i in range(0,N+1):
        t = ti(i,x_0)
        t_list.append(t)
    return np.array(t_list)

def ti_sin (i, x_0):
    return (-1)**i*((x_0**(2*i+1))/math.factorial(2*i+1))

def visualize(t):
    for i in range(0,2*math.pi): #change from len (t) to 2*pi
        plt.plot(i, math.log(abs(t[i])),'ro',)
    plt.xlabel('i')
    plt.ylabel('log')
    plt.show()
    #plot the log(abs(t[i]) 
    
t = terms(ti_sin,3.0,12)
print t
visualize(t)