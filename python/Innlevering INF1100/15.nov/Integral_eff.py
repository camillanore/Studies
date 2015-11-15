# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:03:48 2015

@author: NBCNO1
"""

"""
7.22 (Integral_eff.py, side 438)

Exercise 7.22: Speed up repeated integral calculations

The observant reader may have noticed that our Integral class from
Section 7.3.3 is very inefficient if we want to tabulate or plot a function
F(x) = � x
a f(x) for several consecutive values of x, say x0 < x1 < · · · <
xn. Requesting F(xk) will recompute the integral computed as part of
F(xk−1), and this is of course waste of computer work. Use the ideas from
Section A.1.7 to modify the __call__ method such that if x is an array,
assumed to contain coordinates of increasing value: x0 < x1 < · · · < xn,
the method returns an array with F(x0), F(x1), . . . , F(xn) with the
minimum computational work. Filename: Integral_eff.py
"""
from math import sin, pi, exp
def main():
    a = 0; n = 200
    F = Integral(f,a,n)
    print F(x)
    G = Integral(sin, 0, 200)
    value = G(2*pi)

def f(x):
    return exp(-x**2)*sin(10*x)

def trapezoidal(f, a, x, n):
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

if __name__ == '__main__':
    main()
    