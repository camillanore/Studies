# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 22:43:48 2015

@author: Camilla Nore

"""

# Exercise 2.16: Store data in a nested list

import numpy as np
import matplotlib.pyplot as plt


k_gravity = 9.81 #ms**2
v_0 = 10        #ms
n = 10        # Steps in simulation
end_time_s = 2*v_0/k_gravity

def find_y_t( t, initial_velocity_ms = v_0):
    return initial_velocity_ms * t - 0.5*k_gravity*t**2

print 'Position after', end_time_s, 'second', find_y_t(end_time_s)
data = np.zeros((n+1,2))    

data[:,0] = np.linspace(0, end_time_s, num=n+1)
print data

# Calculate and fill in values in y
for i in range( len(data)):
    data[i,1] = find_y_t(data[i,0])
    
 # Print out the values, and try using zip   
for (time, height) in data:
    print ('t = '+ format(time,'.2f')+
           '\ty = '+ format(height,'.2f'))
           
plt.figure('Ball vertical position')
plt.plot(data[:,0],data[:,1])
