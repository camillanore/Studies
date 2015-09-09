# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 14:31:30 2015

@author: Camilla Nore
"""

"""Todays exercises:
# 2.2 (f2c_approx_table.py, side 84), 
# 3.3 (roots_quadratic.py, side 129), 
# 3.11 (area_triangle.py, side 134), 
# 3.16 (gaussian2.py, side 136), 
# 3.23 (Heaviside.py, side 139

# Exercise 2.2: Generate an approximate Fahrenheit-Celsius
# conversion table

# Many people use an approximate formula for quickly converting Fahrenheit
# (F) to Celsius (C) degrees:
    
# C ≈ C_approx = (F − 30)/2 (2.2)
"""

F = 0
dF = 10
while F <= 100:                
    C = (F-32)*(5.0/9)
    C_approx = (F-30)/2
    print "%5.1f %5.1f %5.1f" %(F, C, C_approx)  
    F = F + dF                    
print '------------------' 

"""Example output:
terminal> python f2c_approx_table.py
  0.0 -17.8 -15.0
 10.0 -12.2 -10.0
 20.0  -6.7  -5.0
 30.0  -1.1   0.0
 40.0   4.4   5.0
 50.0  10.0  10.0
 60.0  15.6  15.0
 70.0  21.1  20.0
 80.0  26.7  25.0
 90.0  32.2  30.0
100.0  37.8  35.0
------------------
"""