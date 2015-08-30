# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:43:54 2015

@author: Camilla Nore
"""

# Exercise 1.10: Calculate the gaussian

def gaussian(x, m=0, s=2):
    f = 1/math.sqrt(2*np.pi*s) * math.exp(-.5*((x-m)/s)**2.0)
    return f

print gaussian(1)

print gaussian(x=1, m=3, s=1)