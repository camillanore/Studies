# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:03:48 2015

@author: Camilla Nore
"""

"""
7.22 (Integral_eff.py, side 438)

Exercise 7.22: Speed up repeated integral calculations

The observant reader may have noticed that our Integral class from
Section 7.3.3 is very inefficient if we want to tabulate or plot a function
F(x) = � x
a f(x) for several consecutive values of x, say x0 < x1 < · · · <
xn. Requesting F(xk) will recompute the integral computed as part of
F(xk−1), and this is of course waste of computer work. 

Use the ideas from
Section A.1.7 to modify the __call__ method such that if x is an array,
assumed to contain coordinates of increasing value: x0 < x1 < · · · < xn,
the method returns an array with F(x0), F(x1), . . . , F(xn) with the
minimum computational work. Filename: Integral_eff.py
"""
from math import sin, pi, exp
import numpy as np
def main():
    a = 0; n = 200
    F = Integral(f,a,n)
    x = [1, 2, 3]
    #G = Integral(sin, 0, 200)
    #value = G(2*pi)
    test_integral()
    
def f(x):
    return x**2

def f_integral_analytical(x0,x1):
        """ """
        return (1/3.0)*(x1**3 - x0**3)
def trapezoidal(f, a, x, n):
    """ The trapezoid integran of f(x) from x(to) = a to x(t) = x
    """
    h = (x-a)/float(n)
    I = 0.5*f(a)
    for i in range(1, n):
        I += f(a + i*h)
    I += 0.5*f(x)
    I *= h
    return I

class Integral:
    def __init__(self, f, a, n= 100):
        self.f, self.a, self.n =f, a, n
    
    def __call__(self, x):
        return trapezoidal(self.f, self.a, x, self.n)

class Integral_eff:
    """ Compute the integral for the vector of x values.
    Return a vector of integralc, corresponding to the x1, x2 ...xn
    """
    def __init__(self, f, a, n= 100):
        self.f, self.a, self.n =f, a, n
    
    def __call__(self, x):
        x_values = [self.a] + x        
        integrals = np.zeros(len(x_values))
        for i in range(len(x_values)-1):
            # We exploit the fact that x is increasing, and we can use the last value.
            integrals[i+1] = (integrals[i] + trapezoidal(self.f,
                                                          x_values[i],
                                                          x_values[i+1], 
                                                          self.n )) # *
        return integrals[1:]
        
def test_integral():
    x_0 = 0.0
    integrator = Integral_eff(f, x_0, n = 500) # n is default 100
    x_values = [1.0, 2.0, 3.0, 4.0]
    integrals_expected = [f_integral_analytical(x_0, xi) for xi in x_values]    
    integrals_computed = integrator(x_values)
    
    np.testing.assert_array_almost_equal(integrals_expected,
                                         integrals_computed,
                                         decimal = 5,
                                         err_msg='Integral failed')
                        
    print 'Test successfull!'
    print 'Analytical result:', integrals_expected
    print 'Computed result:', integrals_computed
    print 'Error in result:', integrals_expected - integrals_computed

if __name__ == '__main__':
    main()
    
"""Output:
Test successfull!
Analytical result: [0.3333333333333333, 2.6666666666666665, 9.0, 21.333333333333332]
Computed result: [  0.333334   2.666668   9.000002  21.333336]
Error in result: [ -6.66666667e-07  -1.33333333e-06  -2.00000000e-06  -2.66666667e-06]

*Comment: Since we keep n constant for each call to trapezoidal, 
this method does not actually reduce the computational load. 
I.e. the number of loop iterationsin trapezoidal are the same. 
However we do increase presision. To reduce computational
load, we would have to compute an n-vale for each step in __call__. 
"""