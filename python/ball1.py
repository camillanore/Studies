# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# INF1100 Obligatorisk gruppeoppgaver


print 5*0.6 - 0.5*9.81*0.6**2

from numpy import *

def integrate(f, a, b, n=100):
    """
    Integrate f from a to b,
    using the Trapezoidal rule with n intervals.
    """
    x = linspace(a, b, n+1)    # Coordinates of the intervals
    h = x[1] - x[0]            # Interval spacing
    I = h*(sum(f(x)) - 0.5*(f(a) + f(b)))
    return I

# Define my special integrand
def my_function(x):
    return exp(-x**2)

minus_infinity = -20  # Approximation of minus infinity
I = integrate(my_function, minus_infinity, 1, n=1000)
print 'Value of integral:', I

v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print y

initial_velocity = 5
accel_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - \
                         0.5*accel_of_gravity*TIME**2
print VerticalPositionOfBall

# program for computing the height of a ball
# in vertical motion
v0 = 5    # initial velocity
g = 9.81  # acceleration of gravity
t = 0.6   # time
y = v0*t - 0.5*g*t**2  # vertical position
print y