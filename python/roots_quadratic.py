# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 14:52:26 2015

@author:Camilla Nore
"""

""" Exercise 3.3 Roots-quadratic

Exercise 3.3: Write a function for solving ax2 + bx + c = 0

a) Given a quadratic equation ax2+bx+c = 0, write a function roots(a,
b, c) that returns the two roots of the equation. The returned roots
should be float objects when the roots are real, otherwise the function
returns complex objects.

Hint. Use sqrt from the numpy.lib.scimath library, see Chapter 1.6.3.

b) Construct two test cases with known solutions, one with real roots
and the other with complex roots, Implement the two test cases in two
test functions test_roots_float and test_roots_complex, where you
call the roots function and check the type and value of the returned
objects.

Find the roots of the quadratic equation ax² + bx + c = 0
    The solution is the equation:
        -b ± √(b² - 4ac)
    x = ----------------
                 2a

"""
import numpy as np
import numpy.lib.scimath as npsci

def main():
    print "Running Roots Quadratic, to test, please use:"
    print "nosetests roots_quadratic.py -v -s"
    print "---"
    print "Example, the roots of x^2 - 2x +2 =0 is:"
    print roots(1,-2,2)
    print "..."
    print "Running tests from main function:"
    test_sqrt()
    print type(npsci.sqrt(-1) + 1)
    print type(5 +1j)
    print roots(1,2,3)
    tests_roots_complex()
    tests_roots_real()
    print "All tests passed. BOOM!"
    
def roots(a, b, c):
    """Find the roots and solution to the equation on the form
    ax² + bx + c = 0

    The solution is the equation:
             √(b² - 4ac)
    x = -b ± -----------
                 2a

    """
    root_part = npsci.sqrt(b**2 - 4*a*c)
    x1 = (-b + root_part)/(2*a)
    x2 = (-b - root_part)/(2*a)
    return (x1, x2)
    
def test_sqrt():
    assert npsci.sqrt(-1)==1j, 'sqrt not working as suspected'
    
def tests_roots_real():
    """Test with real roots"""
    r1 = 1.0
    r2 = 1.0
   # x^2 - (r1+r2)x + r1*r2 = 0
    
    a = 1
    b = -(r1 + r2)
    c = r1*r2
    result = roots(a, b, c)
    print '(a,b,c) --> (x1,x2):'
    print (a,b,c), '-->', result
    #Warning: The order is important, let r1 be the biggest root.
    assert result == (r1, r2), ('Expected:' + str((r1,r2)) +
                                'Result is: ' + str(result))  
    assert isinstance(result[0], float), 'Expected float root'
    assert isinstance(result[1], float), 'Expected float root'

def tests_roots_complex():
    """Test with complex roots"""
    r1 = 1.0 + 1.0j
    r2 = 1.0 - 1.0j
   # x^2 - (r1+r2)x + r1*r2 = 0
    
    a = 1
    b = -(r1 + r2)
    c = r1*r2
    result = roots(a, b, c)
    print '(a,b,c) --> (x1,x2):'
    print (a,b,c), '-->', result
    print type(result[0])
    assert result == (r1, r2), ('Expected:' + str((r1,r2)) +
                                'Result is: ' + str(result))
    assert isinstance(result[0], complex), 'Expected complex root'
    assert isinstance(result[1], complex), 'Expected complex root'
# NB!: The main shall always be the last
if __name__=='__main__':
    """If this python script is run directly"""
    main()  

"""
Example from running as script:

----------------------------------------------------------------------
Ran 3 tests in 0.019s

OK

Running Roots Quadratic

C:\Users\NBCNO1\Documents\Studies\python>nosetests roots_quadratic.py -s -v
roots_quadratic.test_sqrt ... ok

roots_quadratic.tests_roots_real ... Test real roots: (a,b,c) --> (x1,x2):
(1, -2.0, 1.0) --> (1.0, 1.0)
ok
roots_quadratic.tests_roots_complex ... Test complex roots: (a,b,c) --> (x1,x2):
(1, (-2-0j), (2+0j)) --> ((1+1j), (1-1j))
<type 'numpy.complex128'>
ok

Example from running in python:

'C:/Users/NBCNO1/Documents/Studies/python')
Running Roots Quadratic, to test, please use:
nosetests roots_quadratic.py -v -s
---
Example, the roots of x^2 - 2x +2 =0 is:
((1+1j), (1-1j))
...
Running tests from main function:
<type 'numpy.complex128'>
<type 'complex'>
((-1+1.4142135623730951j), (-1-1.4142135623730951j))
(a,b,c) --> (x1,x2):
(1, (-2-0j), (2+0j)) --> ((1+1j), (1-1j))
<type 'numpy.complex128'>
(a,b,c) --> (x1,x2):
(1, -2.0, 1.0) --> (1.0, 1.0)
All tests passed. BOOM!

"""