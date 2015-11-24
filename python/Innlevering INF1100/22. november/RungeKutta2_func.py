# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:19:30 2015

@author: Camilla Nore
"""
"""
E.30 (RungeKutta2_func.py, side 778), 

Exercise E.30: Implement a 2nd-order Runge-Kutta method;
function

Implement the 2nd-order Runge-Kutta method specified in formula (E.38).
Use a plain function RungeKutta2 of the type shown in Section E.1.2 for
the Forward Euler method. Construct a test problem where you know the
analytical solution, and plot the difference between the numerical and
analytical solution. Demonstrate that the numerical solution approaches
the exact solution as Δt is reduced. Filename: RungeKutta2_func.py

"""
import numpy as np
import matplotlib.pyplot as plt 
import math

def RungeKutta2_func(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    dt2 = dt/2
    for k in range(n):         
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + K2 
    return u, t
       

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

# Problem: u'=u
def f(u, t):
    """The simplest thinkable differential equation f.
        Analytival solution of this is f(t) = exp(t)"""
    return u

def main():
    """ Demonstrate that the numerical solution approaches the exact solution
        as dt is reduced."""
    
    N_values = [3, 7, 20]
    plt.figure('rk2')
    for n in N_values:        
        rk2, trk2 = RungeKutta2_func(f, U0=1, T=4, n=n)
        plt.plot(trk2, rk2, '--', label='Runge Kutta 2, N=' + str(n))
         
    #Plot the exact solution
    u, t = ForwardEuler(f, U0=1, T=4, n=20)       
    plt.plot(t, u, label='Forward Euler, N=20')
    u_exact = np.exp(t)
    plt.plot(t, u_exact, label='Exact solution')
    plt.xlabel='t' 
    plt.ylabel='u'
    plt.legend(loc='best')
    plt.title('Solution of the ODE u=u, u(0)=1')
    plt.show()
    #plt.savefig='tmp.pdf'

if __name__ == '__main__':
    main()

""" Output:

I denne oppgaven viser jeg visuelt i plottet hvordan RK-2 blir bedre og bedre
etter som vi øker N, og reduserer dt.

Jeg har også tatt med ForwardEuler for sammenlikning. RK2 er med N=5 
bedre enn Euler med N=20!
""" 