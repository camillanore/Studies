# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:32:19 2015

@author: Camilla Nore
"""

"""
E.16 (radioactive_decay.py, side 773, 2 poeng)

Exercise E.16: Simulate radioactive decay

The equation u' = −au is a relevant model for radioactive decay, where
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
decay for T = 20 000 y. Plot the solution. Write out the final u(T) value
and compare it with the exact value e**(−aT).

Filename: radioactive_decay.py.

"""
import numpy as np
import matplotlib.pyplot as plt
import ODESolver

class Decay():
    def __init__(self, mean_lifetime):
        self.a = 1.0/mean_lifetime #1/years
    def __call__(self, u, t=0.0):
        """Return du/dt"""
        return -self.a*u

def main():
    mean_lifetime_c14 = 5600/np.log(2) # years
    print 'Mean lifetime of Carbon-14', mean_lifetime_c14
    decay_obj = Decay(mean_lifetime_c14)
    rk4_obj = ODESolver.RungeKutta4(decay_obj)
    rk4_obj.set_initial_condition(1.0)    
    
    # Compute numerical solution
    timestep = 500
    T_final = 20000
    t_years = np.asarray(range(0,20500,timestep))
    u, t = rk4_obj.solve(t_years)
    
    # Compare exact and numerical solution
    exact_value = np.exp(-(1.0/ mean_lifetime_c14 * T_final))
    print 'Exact solution:', exact_value
    print 'RK4 solution:', u[-1]
    
    # Plot the decay
    plt.plot(t, u, label = 'Rungekutta4')
    plt.plot(t, np.exp(-1/mean_lifetime_c14*t), label ='Exact solution')
    plt.xlabel('Years')
    plt.ylabel('Radioactive particles')
    plt.title('Radioactive decay for Carbon-14')
    plt.show()
    
if __name__ == '__main__':
    main()    
    
"""Output:
Mean lifetime of Carbon-14 8079.09222898
Exact solution: 0.0841187620395
RK4 solution: 0.084118788845
"""