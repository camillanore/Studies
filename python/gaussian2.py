# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:32:24 2015

@author: Camilla Nore
"""
"""
.16 (gaussian2.py, side 136), 3.23 (Heaviside.py, side 139)
"""
# Exercise 3.16 Implement a gaussian function


import pylab
import numpy as np
import math

def main():
    table = gaussian_table(n=12)
    print_table(table)
    
def gaussian(x, m=0, s=2):
    f = 1/math.sqrt(2*np.pi*s) * math.exp(-.5*((x-m)/s)**2.0)
    return f

def gaussian_table(m=0, s=2, n=10):
    table = np.zeros((n,2))
    xmin = m - 5*s
    xmax = m + 5*s
    xstep = (xmax - xmin) / float(n-1)
    print "xstep:", xstep, "min,max", xmin, xmax
    for index in range(n):
        x = xmin + xstep*index
        f = gaussian(x, m=m, s=s)
        table[index, :] = [x, f]
        #print index
    return table
    
def print_table(table):
    print "----------------"
    print "    x      f(x)"
    print "----------------"    
    for i in range(len(table)):
        print "%6.2f  %6.6f" % (table[i,0],table[i,1])
    print "----------------" 
    
if __name__ == "__main__":
    main()

"""Output:
xstep: 1.81818181818 min,max -10 10
----------------
    x      f(x)
----------------
-10.00  0.000001
 -8.18  0.000066
 -6.36  0.001787
 -4.55  0.021319
 -2.73  0.111329
 -0.91  0.254408
  0.91  0.254408
  2.73  0.111329
  4.55  0.021319
  6.36  0.001787
  8.18  0.000066
 10.00  0.000001
----------------
"""