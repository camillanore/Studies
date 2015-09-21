# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:26:14 2015

@author: Camilla Nore
"""
"""
Eksample: Use linspace when given a task e.g: Make n uniformly spaced values between 0 and 10.
"""
import numpy as np
"""
a = 0 # [s]
b = 10 # [s] 
n = 100
t = np.linspace(a, b, n) #lager uniformt verdier mellom a og b

print t

print[1]

v_0 = 0.6 # [m/s]
g = 9.81 # [m/s^2]

y = v_0*t - 0.5 * g * t**2 # multiplies all elements in t with 5

print y

Today:
use 
np.array (when knowing the values)
np.zeros (empty array)
np.linspace (uniformly values)
eg:
x = np.zeros()
for i in range(len(x)):
    x[i] = 5
"""

import math
import numpy as np

a = 0
b = 10
n = 100

t = np.linspace(a, b, n) # this is an array. Mostly used
y = np.sin(t) # When using np you know it is a vector
# y = np.zeros will create an empty array
print t
print[1]

from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, axis
plot(t, y, 'xr', label="y")
plot(t, y*2, label="y*2")
xlabel('t [s]')
ylabel('amplitude')
legend(loc='best') #have to name the graph. Best place in the graph(not defaut)
axis([-5, 5, -2, 2]) #if you want to zoom in on the graph
show() #This will make the graph

