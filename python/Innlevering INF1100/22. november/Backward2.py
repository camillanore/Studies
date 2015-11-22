# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:31:09 2015

@author: NBCNO1
"""

"""
9.11 (Backward2.py, side 595), 

Exercise 9.11: Implement a new subclass for differentiation

A one-sided, three-point, second-order accurate formula for differentiating
a function f(x) has the form
f�
(x) ≈ f(x − 2h) − 4f(x − h) + 3f(x)
2h . (9.17)
Implement this formula in a subclass Backward2 of class Diff from
Section 9.2. Compare Backward2 with Backward1 for g(t) = e−t for
t = 0 and h = 2−k for k = 0, 1, . . . , 14 (write out the errors in g�
(t)).
Filename: Backward2.py.
"""