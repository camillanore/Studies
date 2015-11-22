# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:10:05 2015

@author: NBCNO1
"""
"""
Exercise 9.6: Make super- and subclass for a point

A point (x, y) in the plane can be represented by a class:

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
            return ’(%g, %g)’ % (self.x, self.y)

We can extend the Point class to also contain the representation of the
point in polar coordinates. To this end, create a subclass PolarPoint
whose constructor takes the polar representation of a point, (r, θ), as 
arguments. Store r and θ as attributes and call the superclass constructor
with the corresponding x and y values (recall the relations x = r cos θ
and y = r sin θ between Cartesian and polar coordinates). Add a __str__
method in class PolarPoint which prints out r, θ, x, and y. Verify the
implementation by initializing three points and printing these points.
Filename: PolarPoint.py.

"""
import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
print 'x:', self.x
print 'y:', self.y    

class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        Point.__init__(self,x,y)
    
    def __str__(self):
        r, theta, x, y = self.r, self.theta, self.x, self.y
        return 'Polar: (%g, %g), Cartesian: (%g,%g)' % (r, theta, x, y)
origo1 = Point(0,0)
origo2 = PolarPoint(0,1)

print origo1
print origo2