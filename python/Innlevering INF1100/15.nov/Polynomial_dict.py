# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:03:09 2015

@author: NBCNO1
"""

"""
7.28 (Polynomial_dict.py, side 440)
Use a dictionary for the coeff attribute in class Polynomial from Section
7.3.7 such that self.coeff[k] holds the coefficient of the xk term.
The advantage with a dictionary is that only the nonzero coefficients
need to be stored.
a) Implement a constructor and the __add__ method.
b) Implement the __mul__ method.
c) Write a test function for verifying the implementations in a) and
b) when the polynomials x − 3x100 and x20 − x + 4x100 are added and
multiplied
"""

class Polynomial_dict:
    def __init__(self, coefficients):
        input_type = type(coefficients)
        if input_type == list:
            #We assume that the list contain the coefficients in order.
            self.coeff = {k: coefficients[k] for k in range(len(coefficients))}
        elif input_type == dict:
            self.coeff = coefficients
        else:
            print 'Not supported input type'
        
    def __call__(self, x):
        taylor_sum = 0
        for key in self.coeff.keys():
            taylor_sum += self.coeff[key]*x**key
        return taylor_sum
    
    def __add__(self, other):
        common_keys = [key for key in self.coeff.keys()
                        if key in other.coeff.keys()]
        result_coeff = self.coeff.copy()
        result_coeff.update(other.coeff)
        #For equal values, other will overwrite the existing value.
        for key in common_keys:
            result_coeff[key] = self.coeff[key] + other.coeff[key]
        print 'common keys', common_keys
        return Polynomial_dict(result_coeff)
    
        #Start with the longest list and add in the other
    def __mul__(self, other):
        #(x + x^2)(1+ 2x) = x(1+ 2x) + x^2(1 + 2x)
        result_coeff = {}
        for k1 in self.coeff.keys():
            for k2 in other.coeff.keys():
                exponent = k1 + k2
                coefficient = self.coeff[k1]*other.coeff[k2]
                if exponent in result_coeff.keys():
                    coefficient += result_coeff[exponent]
                result_coeff[exponent] = coefficient
        return Polynomial_dict(result_coeff)

def test_Polynomial_dict_init():
    #Check that init works with both list and dict.
    coeff1 = {1: 1, 100: -3}
    pol1 = Polynomial_dict(coeff1)
    for key in coeff1.keys():
        assert coeff1[key] == pol1.coeff[key], 'Coefficient error'
    print 'Test init with dict successful.'
    
def test_Polynomial_dict_init_list():
    #Check that init works with list.
    # Pol: 1 + 2x + 3x^2 + 4x^3
    coeff = [1, 2, 3, 4]
    pol = Polynomial_dict(coeff)
    for k, coefficient_k in enumerate(coeff):
        assert coefficient_k == pol.coeff[k], 'Coefficient initializing error'
    #Test that output is right
    x = 2.3
    expected_out = 1 + 2*x +  3*x**2 + 4*x**3
    result = pol(x)
    assert expected_out == result, 'Error in polynomial result.'
    print 'Test init with list successful!'
    
def test_Polynomial_dict_add():
    #Create two polynomial objects, and add them together
    # Pol 1: x - 3x^100
    coeff1 = {1: 1, 100: -3}
    # Pol 2: x^20 - x + 4x^100
    coeff2 = {20: 1, 1: -1, 100: 4}
    pol1 = Polynomial_dict(coeff1)
    pol2 = Polynomial_dict(coeff2)
    pol_sum = pol1 + pol2
    x =2.3
    expected_out = pol1(x) + pol2(x)
    result = pol_sum(x)
    print 'Test add:', result, expected_out
    assert expected_out == result, 'Error in Polynomial add.'
    print 'Test add polynomial successful!'

    
def test_Polynomial_dict_mul():
    #Create two polynomial objects, and multiply them.
    # Pol 1: x - 3x^100
    coeff1 = {1: 1, 100: -3}
    # Pol 2: x^20 - x + 4x^100
    coeff2 = {20: 1, 1: -1, 100: 4}
    pol1 = Polynomial_dict(coeff1)
    pol2 = Polynomial_dict(coeff2)
    pol_mul = pol1 * pol2
    x = 2.33
    expected_out = pol1(x) * pol2(x)
    result = pol_mul(x)
    print 'Test mul:', result, expected_out
    assert expected_out == result, 'Error in Polynomial_mul.'
    print 'Test multiply polynomial successful!'
    
if __name__ == '__main__':
    print 'Running unittests on Polynomial_dict class'
    test_Polynomial_dict_init()
    test_Polynomial_dict_init_list()
    test_Polynomial_dict_add()
    test_Polynomial_dict_mul()

"""Output:
Running unittests on Polynomial_dict class
Test init with dict successful.
Test init with list successful!
common keys [1, 100]
Test add: 1.48861915064e+36 1.48861915064e+36
Test add polynomial successful!
Test mul: -3.55112084184e+74 -3.55112084184e+74
Test multiply polynomial successful!
"""