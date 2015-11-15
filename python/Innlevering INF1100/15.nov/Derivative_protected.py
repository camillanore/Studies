# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:00:30 2015

@author: NBCNO1
"""
"""
Exercise 7.18: Modify a class for numerical differentiation

Make the two attributes h and f of class Derivative from Section 7.3.2
protected as explained in Section 7.2.1. That is, prefix h and f with
an underscore to tell users that these attributes should not be accessed
directly. Add two methods get_precision() and set_precision(h)
for reading and changing h. Filename: Derivative_protected.py.:
"""
def f(x):
    return x**3
 
class Derivative:
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)
    def __call__(self, x):
        f, h = self._f, self._h  #make short forms
        return (f(x+h) - f(x))/h
    def get_precision(self):
        return self._h
    def set_precision(self, h):
        self._h = h
        
dfdx = Derivative(f)
x = 2
print dfdx.get_precision()
dfdx.set_precision(1E-9)
print dfdx(x)

"""
Printed output:
1e-05
12.0000009929
"""