# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:30:50 2015

@author: Camilla Nore
"""

# Math game, choose a number

import sys

number = 42

while True:
    answer = raw_input("Gjett et tall")       #String
    guessed_number = int(answer)               #float or int, choose suitable
    if guessed_number < number:
        print "too low"
    elif guessed_number > number:
        print "too high"
    else:                           #Equivalent: elif guessed_number == number
        print "correct"
        sys.exit()
try:
    answer = raw_input("n = 2")
    n = int(answer)          #Raises exception ValueError

except ValueError:
    n = 1

print n**25