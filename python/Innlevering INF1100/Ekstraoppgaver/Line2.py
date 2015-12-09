# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:22:21 2015

@author: Camilla Nore

Exercise 7.7 Flexible handling of function arguments

"""
class Line:
    def __init__(self, p1, p2):
        """ Initialize a line from two points. 
            Solve for ax + b = y
            NB: This class does not handle vertical lines, i.e. a = infinity.
        """
        if isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
           dx = float(p2[0] - p1[0])
           dy = float(p2[1] - p1[1])
           self.a = dy/dx
           self.b = p1[1] - p1[0]*self.a
        elif isinstance(p1, (tuple,list)) and isinstance(p2, (float,int)):
            # p1 is a point and p2 is slope
            self.a = float(p2)
            self.b = p1[1] - p1[0]*self.a

    def __call__(self, x):
        return self.value(x)

    def value(self, x):
        return self.a*x + self.b

def test_line_with_points():
    from numpy.testing import assert_allclose
    print 'Test Line class with set of points.'
    testpoints = [[(0.0, 0.0), (1.0, 1.0)],   # Easy
                  [(-5.5, 2.0), (-6.0, 1.0)], # Check wrong order
                  [(0.0, 0.0), (1e6, 1.0)],   # Numerically challenging
                  ]
    expected_at1 = [1.0, 15.0, 1e-6]
    for points, check in zip(testpoints, expected_at1):
        line_object = Line(points[0], points[1])
        result = line_object(1.0)
        print " - Input:", points, " Expected:", check, " Result:", result
        assert_allclose( result, check)
    print '-- Test successful!'

def test_line_with_slope():
    print 'Test Line class with point and slope.'
    from numpy.testing import assert_allclose
    testdata = [[(0.0, 0.0), 1.0],   # Easy
                [(-5.5, 2.0), 2.0],  # Check wrong order
                [(1e6, 1.0), 1e-6],  # Numerically challenging
                ]
    expected_at1 = [1.0, 15.0, 1e-6]
    for data, check in zip(testdata, expected_at1):
        line_object = Line(data[0], data[1])
        result = line_object(1.0)
        print " - Input:", data, " Expected:", check, " Result:", result
        assert_allclose( result, check)
    print '-- Test successful!'

if __name__ == '__main__':
    # Run both tests
    test_line_with_points()
    test_line_with_slope()

"""Output:
We can use nosetests, or run this as a python program:

> nosetests line2.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.030s
OK

> python line2.py
Test Line class with set of points.
 - Input: [(0.0, 0.0), (1.0, 1.0)]  Expected: 1.0  Result: 1.0
 - Input: [(-5.5, 2.0), (-6.0, 1.0)]  Expected: 15.0  Result: 15.0
 - Input: [(0.0, 0.0), (1000000.0, 1.0)]  Expected: 1e-06  Result: 1e-06
-- Test successful!
Test Line class with point and slope.
 - Input: [(0.0, 0.0), 1.0]  Expected: 1.0  Result: 1.0
 - Input: [(-5.5, 2.0), 2.0]  Expected: 15.0  Result: 15.0
 - Input: [(1000000.0, 1.0), 1e-06]  Expected: 1e-06  Result: 1e-06
-- Test successful!
"""