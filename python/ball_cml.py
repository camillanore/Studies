# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:30:52 2015

@author: Camilla Nore
"""
"""
Exercise 4.10: Read parameters in a formula from the
command line
Modify the program listed in Exercise 4.9 such that v0 and t are read
from the command line. Filename: ball_cml.py.
"""

# Exercise 4.10: Read parameters in a formula from the command line
import sys

print sys.argv[0]

def y_t(g, t, v_0):
    y = v_0*t - 0.5*g*t**2
    return y

g = 9.81
t = float(sys.argv[1])
v_0 = float(sys.argv[2])
   
print "The solution for y is ", y_t(g, t, v_0)
"""
Output:
ball_cml.py
The solution for y is  0.0342
"""