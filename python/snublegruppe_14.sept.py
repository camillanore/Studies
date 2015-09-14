# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:47:14 2015

@author: 
"""
"""
Snublegruppe 14. september

Oppgave 1

Skriv et program som løser en andregradsligning 

ax^2 + bx + c = 0

Ta i mot koeffisientene ved å bruke raw_input.

Oppgave 2

Samme som oppgave 1, men nå skal bruker oppgi koeffisientene på
kommandolinjen.

Oppgave 3

Utvid oppgave 2 slik at programmet sjekker at koeffisientene faktisk
er tall (hint: exceptions) og at nok argumenter oppgis.

Oppgave 4

Vi tillater nå kun reele røtter. Dersom koeffisientene leder til 
imaginære røtter skal ValueError exception raises med en passende 
feilmelding.
"""

# Oppgave 1
import math
from math import sqrt
import sys
import numpy as np
import numpy.lib.scimath as npsci

print """
This program solves a 2nd degree eq. on the form ax^2 + bx + c = 0, 
where a, b and c are arbitrary constants.
"""

a = float(raw_input("a = "))
b = float(raw_input("b = "))
c = float(raw_input("c = "))

def quadratic_solver(a, b, c):
    
    x1 = (-b + npsci.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - npsci.sqrt(b**2 - 4*a*c))/(2*a)

    return x1, x2

roots = quadratic_solver(a, b, c)

print "\nx1 = %g   ::   x2 = %g" %(roots[0], roots[1])


# Oppgave 2

#from math import sqrt
#import sys

# print This program solves a 2nd degree eq. on the form ax^2 + bx + c = 0, 
#where a, b and c are arbitrary constants.


a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

def quadratic_solver(a, b, c):
    x1 = (-b + npsci.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - npsci.sqrt(b**2 - 4*a*c))/(2*a)

    return x1, x2

roots = quadratic_solver(a, b, c)

print "\nx1 = %g   ::   x2 = %g" %(roots[0], roots[1])


# Oppgave 3

#from math import sqrt
#import sys

#print "This program solves a 2nd degree eq. on the form ax^2 + bx + c = 0, where a, b and c are arbitrary constants."

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except:
    print "a, b and c need to be numbers. E.g. a = 2, b = 4, c = 2"
    a = float(raw_input("a = "))
    b = float(raw_input("b = "))
    c = float(raw_input("c = "))

def quadratic_solver(a, b, c):
    x1 = (-b + npsci.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - npsci.sqrt(b**2 - 4*a*c))/2*a

    return x1, x2

roots = quadratic_solver(a, b, c)

print "\nx1 = %g   ::   x2 = %g" %(roots[0], roots[1])


# Oppgave 4

#from math import sqrt
#import sys

#print "This program solves a 2nd degree eq. on the form ax^2 + bx + c = 0, where a, b and c are arbitrary constants."

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except:
    print "a, b and c need to be numbers. E.g. a = 2, b = 4, c = 2"
    a = float(raw_input("a = "))
    b = float(raw_input("b = "))
    c = float(raw_input("c = "))

def quadratic_solver(a, b, c):
    try:
        x1 = (-b + npsci.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - npsci.sqrt(b**2 - 4*a*c))/2*a
    except ValueError:
        print "\nComplex roots!\n"
        sys.exit(1)

    return x1, x2

roots = quadratic_solver(a, b, c)

print "\nx1 = %g   ::   x2 = %g" %(roots[0], roots[1])