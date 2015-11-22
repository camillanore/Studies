# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:29:58 2015

@author: NBCNO1
"""

"""
9.2 (Cubic_Poly4.py, side 592), 
Exercise 9.2: Make polynomial subclasses of parabolas

The task in this exercise is to make a class Cubic for cubic functions

c_3x**3 + c_2x**2 + c_1**x + c_0

with a call operator and a table method as in classes Line and
Parabola from Section 9.1. Implement class Cubic by inheriting from
class Parabola, and call up functionality in class Parabola in the same
way as class Parabola calls up functionality in class Line.
Make a similar class Poly4 for 4-th degree polynomials
c4x4 + c3x3 + c2x2 + c1x + c0
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
as we make subclasses for higher degree polynomials

"""