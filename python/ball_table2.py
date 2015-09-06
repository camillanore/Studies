# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 14:45:19 2015

@author: Camilla Nore //camilnor
"""
import numpy as np
import matplotlib.pyplot as plt
# Exercise 2.8: Store values from a formula in lists

#This exercise aims to produce the same table of numbers as in Exercise 2.7,
#but with different code. First, store the t and y values in two lists t and
#y. Thereafter, write out a nicely formatted table by traversing the two
#lists with a for loop.

#Hint. In the for loop, use either zip to traverse the two lists in parallel,
#or use an index and the range construction.


# Exercise 2.7 y(t) = v0t − 1/2*gt^2
# Use n + 1 uniformly spaced t values throughout the interval [0, 2v0/g].
# use a for loop to produce the table

k_gravity = 9.81 #ms**2
v_0 = 10        #ms
n = 10        # Steps in simulation
end_time_s = 2*v_0/k_gravity

def find_y_t( t, initial_velocity_ms = v_0):
    return initial_velocity_ms * t - 0.5*k_gravity*t**2

print 'Position after', end_time_s, 'second', find_y_t(end_time_s)
    
t = np.linspace(0, end_time_s, num=n+1)
y = np.zeros(n+1)

# Calculate and fill in values in y
for i in range( len(t)):
    y[i] = find_y_t(t[i])
    
 # Print out the values, and try using zip   
for (time, height) in zip(t,y):
    print ('t = '+ format(time,'.2f')+
           '\ty = '+ format(height,'.2f'))
           
plt.figure('Ball vertical position')
plt.plot(t,y)