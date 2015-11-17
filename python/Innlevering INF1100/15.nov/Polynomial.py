# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:26:22 2015

@author:Camilla Nore
"""

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        taylor_sum = 0
        for i in range(len(self.coeff)):
            taylor_sum += self.coeff[i]*x**i
        return taylor_sum
    
    def __add__(self, other):
        #Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] #copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = self.coeff[:] #copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)