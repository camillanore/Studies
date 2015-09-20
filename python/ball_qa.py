# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:52:51 2015

@author: Camilla Nore
"""
"""
Exercise 4.9: Prompt the user for input to a formula
Consider the simplest program for evaluating the formula y(t) = v0t − 1
2 gt2:
v0 = 3; g = 9.81; t = 0.6
y = v0*t - 0.5*g*t**2
print y
Modify this code so that the program asks the user questions t=? and
v0=?, and then gets t and v0 from the user’s input through the keyboard.

"""
# Exercise 4.9: Prompt the user for input to a formula

import sys


def y_t(g, t, v_0):
    y = v_0*t - 0.5*g*t**2
    return y

g = 9.81
t = float(raw_input("t = ?"))
v_0 = float(raw_input("v_0 = ?"))
   
print "The solution for y is ", y_t(g, t, v_0)

"""
Output:
>>> runfile('C:/Users/NBCNO1/Documents/Studies/python/ball_qa.py', wdir='C:/Users/NBCNO1/Documents/Studies/python')
t = ?0.6
v_0 = ?3
The solution for y is  0.0342
>>> 
"""
