# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:02:53 2015

@author: Camilla Nore
"""
"""
7.23 (Polynomial_exp.py, side 438)

Exercise 7.23: Apply a class for polynomials
The Taylor polynomial of degree N for the exponential function e**x is
given by:
p(x) = sum from k=0 to N over x**k/k!

Make a program that: 
(i) imports class Polynomial from Section 7.3.7,
(ii) reads x and a series of N values from the command line, 
(iii) creates a Polynomial instance representing the Taylor polynomial for each N
value, and 
(iv) prints the values of p(x) for all the given N values as
well as the exact value ex. Try the program out with x = 0.5, 3, 10 and
N = 2, 5, 10, 15, 25. Filename: Polynomial_exp.py
"""
import math
import numpy as np
import sys

# From file Polynomial.py import the class Polynomial
from Polynomial import Polynomial

def main():
    try:
        x_value = float(sys.argv[1])
        N_values = np.asarray(sys.argv[2:], dtype=int)
    except (ValueError, IndexError), e:
        print 'Error:', e
        print 'Usage: %s x_value N1 [N2 N3 ...]' %(sys.argv[0])
        sys.exit(1)
   
    print 'Given x:', x_value
    print 'Given N:', N_values
    print 'Exact value:', math.exp(x_value)
        
    polynomial_objects = []
    for N in N_values:
        coefficients = [(1.0/math.factorial(k)) for  k in range(N)]
        pol_object = Polynomial(coefficients)
        polynomial_objects.append(pol_object)
    
    print ' N      p(x)     exact    error  -- for x = %2.4f'%(x_value)
    for i in range(len(N_values)):
        exact_value = math.exp(x_value)
        polynom_estimate = polynomial_objects[i](x_value)
        error = exact_value - polynom_estimate
        print '%2d  %3.6f  %3.6f  %1.1e'%(N_values[i], 
                                       polynom_estimate,
                                       exact_value,
                                       error)
    print 'Info on machine epsilon float precision:', (np.finfo(float).eps)

def test_main():
    x_values = [0.5, 3.0, 10.0]
    N_values = [2, 5, 10, 15, 25]
    # Modify argv for testing directly not using commandline
    sys.argv = sys.argv + [0.0] + N_values
    for x_val in x_values:
        sys.argv[1] = x_val
        print '\nRunning with input: ' + str(sys.argv[1:])
        main()
if __name__ == '__main__':
    
    if sys.argv[1] == 'Testing':
        test_main()
    else:
        main()

"""Output:
> python Polynomial_exp.py Testing

Running with input: [0.5, 0.0, 2, 5, 10, 15, 25]
Given x: 0.5
Given N: [ 0  2  5 10 15 25]
Exact value: 1.6487212707
 N      p(x)     exact    error  -- for x = 0.5000
 0  0.000000  1.648721  1.6e+00
 2  1.500000  1.648721  1.5e-01
 5  1.648438  1.648721  2.8e-04
10  1.648721  1.648721  2.8e-10
15  1.648721  1.648721  4.4e-16
25  1.648721  1.648721  4.4e-16
Info on machine epsilon float precision: 2.22044604925e-16

Running with input: [3.0, 0.0, 2, 5, 10, 15, 25]
Given x: 3.0
Given N: [ 0  2  5 10 15 25]
Exact value: 20.0855369232
 N      p(x)     exact    error  -- for x = 3.0000
 0  0.000000  20.085537  2.0e+01
 2  4.000000  20.085537  1.6e+01
 5  16.375000  20.085537  3.7e+00
10  20.063393  20.085537  2.2e-02
15  20.085523  20.085537  1.3e-05
25  20.085537  20.085537  6.8e-14
Info on machine epsilon float precision: 2.22044604925e-16

Running with input: [10.0, 0.0, 2, 5, 10, 15, 25]
Given x: 10.0
Given N: [ 0  2  5 10 15 25]
Exact value: 22026.4657948
 N      p(x)     exact    error  -- for x = 10.0000
 0  0.000000  22026.465795  2.2e+04
 2  11.000000  22026.465795  2.2e+04
 5  644.333333  22026.465795  2.1e+04
10  10086.573192  22026.465795  1.2e+04
15  20188.170595  22026.465795  1.8e+03
25  22025.431666  22026.465795  1.0e+00
Info on machine epsilon float precision: 2.22044604925e-16
"""