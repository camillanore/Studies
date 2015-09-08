# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 14:41:53 2015

@author: NBCNO1
"""

F = 0
dF = 10
while F <= 100:                
    C = (F-32)*(5.0/9)
    print "%5.1f %5.1f" %(F, C)  
    F = F + dF                 
print '------------------' 