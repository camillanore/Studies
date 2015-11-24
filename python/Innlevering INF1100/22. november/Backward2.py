# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:31:09 2015

@author: Camilla Nore
"""

"""
9.11 (Backward2.py, side 595), 

Exercise 9.11: Implement a new subclass for differentiation

A one-sided, three-point, second-order accurate formula for differentiating
a function f(x) has the form
f'(x) ≈ f(x − 2h) − 4f(x − h) + 3f(x)/2h  (9.17)

Implement this formula in a subclass Backward2 of class Diff from
Section 9.2. Compare Backward2 with Backward1 for g(t) = e**−t for
t = 0 and h = 2**−k for k = 0, 1, . . . , 14 (write out the errors in g'(t)).

Filename: Backward2.py
"""
import numpy as np
class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x - 2*h) - 4*f(x - h) + 3*f(x))/(2*h)

def g(t):
    return np.exp(-t)
    
def main():
    t = 0.0
    exact_value = -1 # d/dt e**-t = -e**-t
    print 'h=2^(-k)\terr back1\terr back2' 
    print '--------------------------------'    
    for k in range(0,15):
        h = 2 **(-k)
        back1_obj = Backward1(g, h=h)
        back2_obj = Backward2(g, h=h)
        e1 = back1_obj(t) - exact_value
        e2 = back2_obj(t) - exact_value
        print '2^-%d\t%f\t%f'%(k, e1, e2)

if __name__ == '__main__':
    main()
    
"""Output:
h=2^(-k)	err back1	err back2
--------------------------------
2^-0	-0.718282	0.757964
2^-1	-0.297443	0.123397
2^-2	-0.136102	0.025239
2^-3	-0.065188	0.005726
2^-4	-0.031911	0.001365
2^-5	-0.015789	0.000333
2^-6	-0.007853	0.000082
2^-7	-0.003916	0.000020
2^-8	-0.001956	0.000005
2^-9	-0.000977	0.000001
2^-10	-0.000488	0.000000
2^-11	-0.000244	0.000000
2^-12	-0.000122	0.000000
2^-13	-0.000061	0.000000
2^-14	-0.000031	0.000000
"""