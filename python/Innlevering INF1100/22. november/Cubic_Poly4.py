# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:29:58 2015

@author: Camilla Nore
"""

"""
9.2 (Cubic_Poly4.py, side 592), 
Exercise 9.2: Make polynomial subclasses of parabolas

The task in this exercise is to make a class Cubic for cubic functions

c_3x**3 + c_2x**2 + c_1**x + c_0

with a call operator and a table method as in classes Line and
Parabola from Section 9.1. 
--------Implement class Cubic by inheriting from
class Parabola-----, and call up functionality in class Parabola in the same
way as class Parabola calls up functionality in class Line.

Make a similar class Poly4 for 4-th degree polynomials
c4x**4 + c3x**3 + c2x**2 + c1x + c0

by inheriting from class Cubic. Insert print statements in all the
__call__ to help following the program flow. Evaluate cubic and a
4-th degree polynomial at a point, and observe the printouts from all the
superclasses. Filename: Cubic_Poly4.py.

Remarks. This exercise follows the idea from Section 9.1 where more
complex polynomials are subclasses of simpler ones. Conceptually, a cubic
polynomial is not a parabola, so many programmers will not accept class
Cubic as a subclass of Parabola; it should be the other way around, and
Exercise 9.2 follows that approach. Nevertheless, one can use inheritance
solely for sharing code and not for expressing that a subclass is a kind
of the superclass. For code sharing it is natural to start with the simplest
polynomial as superclass and add terms to the inherited data structure
as we make subclasses for higher degree polynomials.

"""
import numpy as np

class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
 
    def __call__(self, x):
        print ' - In Line __call__'
        return self.c0 + self.c1*x
        
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)  # let Line store c0 and c1
        self.c2 = c2

    def __call__(self, x):
        print ' - In Parabola __call__'        
        return Line.__call__(self, x) + self.c2*x**2


class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)  # let Parabola store c0, c1 and c2     
        self.c3 = c3

    def __call__(self, x):
        print ' - In Cubic __call__'
        return Parabola.__call__(self, x) + self.c3*x**3
        
class Poly4(Cubic): #FIX
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)  # let Poly4 store c0, c1 and c2     
        self.c4 = c4

    def __call__(self, x):
        print ' - In Poly4 __call__'
        return Cubic.__call__(self, x) + self.c4*x**4    

# Taylor series of exp
# f(x) = 1 + x + x**3/2 + x**3/6 + x**4/24
cubic_obj = Cubic(1, 1, 0.5, 1/6.0)
poly4_obj = Poly4(1, 1, 0.5, 1/6.0, 1/24.0)

print 'The Euler number is: ', np.exp(1)
print 'Trace of Cubic.__call__(x=1.0)'
print 'Cubic e result: %f\n' %cubic_obj(1.0) 
print 'Trace of Poly4.__call__(x=1.0)'
print 'Poly4 e result: %f' %poly4_obj(1.0)
    
"""Output:
The Euler number is:  2.71828182846
Trace of Cubic.__call__(x=1.0)
 - In Cubic __call__
 - In Parabola __call__
 - In Line __call__
Cubic e result: 2.666667

Trace of Poly4.__call__(x=1.0)
 - In Poly4 __call__
 - In Cubic __call__
 - In Parabola __call__
 - In Line __call__
Poly4 e result: 2.708333
"""