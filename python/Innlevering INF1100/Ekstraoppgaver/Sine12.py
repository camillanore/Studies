# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:24:26 2015

@author: Camilla Nore

Exercise 9.9: Implement a subclass

"""

""" This is based on the example file src/oo/session.py """

from math import *

class FuncWithDerivatives:
    def __init__(self, h=1.0E-9):
        self.h = h  # spacing for numerical derivatives
    def __call__(self, x):
        raise NotImplementedError('___call__ missing in class %s' % 
                                  self.__class__.__name__)
    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)
    
    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)

class Sine1(FuncWithDerivatives):
    """ Implement sine and rely on the inherited functions for derivatives."""
    def __call__(self, x):
        return sin(x)

class Sine2(FuncWithDerivatives):
    """ Implement sine with analytical derivatives """
    def __call__(self, x):
        return sin(x)
    def df(self, x):
        return cos(x)
    def ddf(self, x):
        return -sin(x)

def main():
    """ Compare Sine1 and Sine2 for computing the 1st and 2nd order 
    derivatives at two x points. """
    print 'Testing the classes for pi/4 and pi/6'
    x_values = (pi/4, pi/6)
    sin1 = Sine1()
    sin2 = Sine2()
    print 'x\t\tdsin1\t\tdsin2\t\tddsin1\t\tddsin2'
    for x in x_values:
        print '%f\t%f\t%f\t%f\t%f'%(x, sin1.df(x), sin2.df(x), 
                                    sin1.ddf(x), sin2.ddf(x))


if __name__ == '__main__':
    main()

""" Output:

> python Sine12.py
Testing the classes for pi/4 and pi/6
x               dsin1           dsin2           ddsin1          ddsin2
0.785398        0.707107        0.707107        111.022302      -0.707107
0.523599        0.866025        0.866025        55.511151       -0.500000

Comment:
The numerical method doesn't do very well on the second dericative.
"""