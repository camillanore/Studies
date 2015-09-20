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

a = 1      # 1st statement (assignment statement)
b = 2      # 2nd statement (assignment statement)
c = a + b  # 3rd statement (assignment statement)
print c    # 4th statement (print statement)

import numpy as np
import math
import pylab
# Exercise 1.10: Calculate the gaussian

def gaussian(x, m=0, s=2):
    f = 1/math.sqrt(2*np.pi*s) * math.exp(-.5*((x-m)/s)**2.0)
    return f

print gaussian(1)

print gaussian(x=1, m=3, s=1)
 
# Exercise 1.11: Compute the air resistance on a football

def air_resistance(velocity,           #m/s
                   radius=0.11,         #m
                   drag_coefficient=0.2):   #no units
                    
    k_air_density = 1.2 # kg/m**3 
    area = np.pi*radius**2
    drag_force = (0.5*drag_coefficient*k_air_density*
                        area*velocity**2)
    return drag_force # N
   
print air_resistance(velocity=4)
print air_resistance(velocity=10)
print air_resistance(velocity=120)

air_drag=[]
velocity=[]
for i in range(0,400):
    velocity.append(i/10.0)
    air_drag.append(air_resistance(i/10.0))
pylab.plot(velocity,air_drag)
pylab.xlabel('Velocity, m/s')
pylab.ylabel('Drag force, N')

def convert_kmh_to_ms( vel_kmh):
   return vel_kmh/3.6 # m/s
   