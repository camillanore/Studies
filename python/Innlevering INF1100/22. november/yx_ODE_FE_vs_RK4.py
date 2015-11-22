# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:31:45 2015

@author: NBCNO1
"""

"""
E.23 (yx_ODE_FE_vs_RK4.py, side 775, 2 poeng),
 
Exercise E.23: Compare ODE methods

Investigate the accuracy of the 4th-order Runge-Kutta method and the
Forward Euler scheme for solving the (challenging) ODE problem:
dy/dt = 1/(2*(y-1))
y(0) = 1 + math.sqrt(epsilon)
x = range (0,1,4) # start, step,stop
where epsilon is a small number, say epsilon = 0.001. 
Start with four steps in [0, 4] and reduce the step size repeatedly by a factor
of two until you find thesolutions sufficiently accurate. 
Make a plot of the numerical solutions
along with the exact solution 
y(x) = 1 + math.sqrt(x + epsilon) for each step size.

Filename: yx_ODE_FE_vs_RK4.py.
"""