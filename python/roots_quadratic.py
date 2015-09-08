# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 14:52:26 2015

@author: NBCNO1
"""

# Exercise 3.3 (roots_quadratic.py, side 129)

#Exercise 3.3: Write a function for solving ax2 + bx + c = 0
#a) Given a quadratic equation ax2+bx+c = 0, write a function roots(a,
#b, c) that returns the two roots of the equation. The returned roots
#should be float objects when the roots are real, otherwise the function
#returns complex objects.

#Hint. Use sqrt from the numpy.lib.scimath library, see Chapter 1.6.3.

#b) Construct two test cases with known solutions, one with real roots
#and the other with complex roots, Implement the two test cases in two
#test functions test_roots_float and test_roots_complex, where you
#call the roots function and check the type and value of the returned
#objects.

import numpy as np
import math
import cmath

# a*x**2 + b*x + c = 0 

#a = float(input('Enter the coefficients of a: '))
#b = float(input('Enter the coefficients of b: '))
#c = float(input('Enter the coefficients of c: '))

def roots(a, b, c):
    d = b**2-4*a*c # Calculating the discriminant

# if d < 0:
#    return ('complex objects') #skjønner ikke 
#else:
#    def x1:
#        return ((-b + np.lib.scimath.sqrt(d)/2*a)
#    def x2:
#        return ((-b - np.lib.scimath.sqrt(d))/2*a)
    if d<0:
        x1 = ((-b + np.lib.scimath.sqrt(d)/2*a)
        x2 = ((-b - np.lib.scimath.sqrt(d))/2*a)
    return x1,x2
    
    else:
        x1 = ((-b + np.lib.scimath.sqrt(d)/2*a)
        x2 = ((-b - np.lib.scimath.sqrt(d))/2*a)
    return x1, x2
    
print (roots(3, -4, 16)
    
#float(x)