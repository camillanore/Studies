# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:26:18 2015

@author: NBCNO1
"""
import matplotlib.pyplot as plt
import numpy as np
import ODESolver

f = lambda x: x**2 #kan bare gjøre en ting, men flere variable

"""Lambda funksjonen er ekvivalent med følgende"""

def f(x):
    return x**2

def f(x):
    y = x**2
    return y - 2 # cannot be written as a lambda function

#Example:

u,t = RungeKutta2(lambda u, t: u) # returnerer u. vil bare bruke den en gang. 

def f(u,t):
    return u
    
u, t = RungeKutta2(f)

# Difflikninger

"""Math def: u'(t) = f(u(t),t). Kan starte baklengs"""
u = zeros(n)
t = zeros(n)
dt = 0.001
#t = linspace (0, T, n)
#T = 10 # [s]
#dt = t[1] - t[0]

u[0] = U0

for k in range (n-1): # check first and last value
    u[k+1] = u[k] + dt* f(u[k], t[k]) # math expression


def f(u,t):
    return -u +1

#Velge hvilken klasse du skal bruke
t = np.linspace (0, T, int(T/dt+1)) #evt bruk ceil eller floor. linspace fikser int,
#det gjør ikke range.  
solver =  ForvardEuler(f) # sjekk input. her funksjonen f
solver.set_initial_condition(0) #set initital condition 

# Hva gir return? u'er og t'er
u, t = solver.solve(t) #tar inn time points som er en array
"""Eksempel: tømme en tank. si at den ikke er gyldig for negative verdier."""
# Show the plot 

plt.plot()
plt.show()

# Lister og diverse
t_list = range(5)
v_list = [4, 1, 9, 2, 5]
#v_list = [[4], [1, 2], [9], [2, 3], [5, 1]] #hvert element er en ny liste. kan 
# da foreta listeoperasjoner. 

for t in t_list:
    print 't=%d' %t

for i in range(len(t_list)):
    print 't=%d v=%v' % (t_list[i], v_list[i])
    
for t, v in zip(t_list, v_list): #fletter sammen og pakkker ut
    print 't=%d v=%d' %(t, v)