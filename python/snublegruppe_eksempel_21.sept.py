# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:43:18 2015

@author: Camilla Nore
"""

"""
OPPGAVE 1:

Lag et program som plotter sin(x), hvor kurven skal bestå av blåe
rundinger. Intervallet kan være [0,4*pi].

OPPGAVE 2:

Lag et program som tar inn en vilkårlig funksjon f(x) enten fra raw_input()
eller sys.argv[], og plotter denne mellom et intervall [a,b]. Gi brukeren
mulighet til å gi a og b via raw_input() eller kommandolinjen.

HINT: StringFunction().

OPPGAVE 3:

Utvid programmet fra oppgave 2 slik at brukeren får et spærsmål om å plotte
den deriverte til funksjonen i samme vindu.

HINT: Lag en funksjon f_der(x) som returnerer den deriverte i et punkt x.
"""
# Exercise 1

from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, axis, title
import math
import numpy as np
"""
a = 0
b = 4*math.pi

x = np.linspace(a, b, 1001)
y = np.sin(x)

plot(x, y, 'ob')
title('y = sin(x)')
legend(loc='best')
xlabel('x') 
ylabel('y')

"""

# Exercise 2


def f(a, b, x, y): 
    
    f = raw_input("Please input function: ")
    a = float(raw_input("Please provide a: "))
    b = float(raw_input("Please provide b: "))
    x = np.linspace(a,b,101)
    y = eval(f)
    y = np.array([f(i) for i in x]) #
    return f
    
plot(x,y)
title('f(x)')
xlabel('x from linspace')
ylabel('y from array')
legend()

"""
#Exercise 3

from scitools.std import *  
from scitools.StringFunction import StringFunction

def f_der(x):
    h = 10**-7
    return (f(x+h) - f(x))/h

func = raw_input("Please input function: ")
f = StringFunction(func)
a = float(raw_input("Please provide a: "))
b = float(raw_input("Please provide b: "))
x = linspace(a,b,101)
y = array([f(i) for i in x])

d = raw_input("Do you want to plot the derivative in the same plot? y/n: ")

if d == "y" or d == "Y":
    y_der = array([f_der(i) for i in x])
    plot(x,y, legend="f(x)" )
    hold("on")
    plot(x,y_der,legend="f'(x)")
else:
    plot(x,y,legend="f(x)")
"""