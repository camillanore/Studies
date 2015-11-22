# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:32:19 2015

@author: NBCNO1
"""

"""
E.16 (radioactive_decay.py, side 773, 2 poeng)

Exercise E.16: Simulate radioactive decay

The equation u**T = −au is a relevant model for radioactive decay, where
u(t) is the fraction of particles that remains in the radioactive substance
at time t. The parameter a is the inverse of the so-called mean lifetime
of the substance. The initial condition is u(0) = 1.

a) Introduce a class Decay to hold information about the physical
problem: the parameter a and a __call__ method for computing the
right-hand side −au of the ODE.

b) Initialize an instance of class Decay with a = ln(2)/5600 1/y. The
unit 1/y means one divided by year, so time is here measured in years,
and the particular value of a corresponds to the Carbon-14 radioactive
isotope whose decay is used extensively in dating organic material that
is tens of thousands of years old.

c) Solve u' = −au with a time step of 500 y, and simulate the radioactive
decay for T = 20, 000 y. Plot the solution. Write out the final u(T) value
and compare it with the exact value e**(−aT).

Filename: radioactive_decay.py.

"""