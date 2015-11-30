# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:43:26 2015

@author: Camilla Nore

Exercise E.43: Introduce vaccination in a SIR model

We shall now extend the SIR model in Exercise E.41 with a vaccination2
program. If a fraction p of the susceptibles per time unit is being vaccinated,
and we say that the vaccination is 100 percent effective, pSΔt
individuals will be removed from the S category in a time interval Δt.
We place the vaccinated people in a new category V. The equations for
S and V becomes:

S' = −βSI − pS, (E.82)
V' = pS .

The equations for I and R are not affected. The initial condition for V
can be taken as V (0) = 0. The resulting model is named SIRV.

Try the same parameters as in Exercise E.41 in combination with
p = 0.1 and compute the evolution of S(t), I(t), R(t), and V (t). Comment
on the effect of vaccination on the maximum number of infected. Filename:
SIRV.py.
"""


import numpy as np
import matplotlib.pyplot as plt
import ODESolver

"""Global values for initial conditions and parameters"""

beta = 0.0005 # Infection rate per day
mu = 0.1      # Recovery rate per day
SIRV_initial = (1500, 1, 0, 0)
p = 0.1

def main():
    print 'SIRV modelling'
    t_days, SIRV = SIRV_solver(beta, mu)
    SIRV_visualize(t_days, SIRV)
    print 'Condition at last day=%d: S=%.f, I=%.f, R=%.0f, V=%.f' %(
        t_days[-1], SIRV[-1,0], SIRV[-1,1], SIRV[-1,2], SIRV[-1,3])
    print 'Maximum number of infected = %d' % SIRV[:,1].max()

def SIRV_solver(beta, mu):
    """ Solve the SIR system, and return a numpy array with t, S, I and R."""
    n_steps = 120
    t = np.linspace(0, 60, n_steps)    
    SIRV = np.zeros((n_steps, 4))
    rk4_obj = ODESolver.RungeKutta4(SIRV_timederivative)
    rk4_obj.set_initial_condition(SIRV_initial)
    SIRV, t = rk4_obj.solve(t, terminate = SIRV_validate)
    return t, SIRV

def SIRV_timederivative(SIRV, t):
    """Return the SIR d/dt values for the given input data [S, I, R]."""       
    Sddt = - beta*SIRV[0]*SIRV[1] - p*SIRV[0]
    Iddt =   beta*SIRV[0]*SIRV[1] - mu*SIRV[1]
    Rddt =                        mu*SIRV[1]
    Vddt =                        p*SIRV[0]
    return [Sddt, Iddt, Rddt, Vddt]

def SIRV_validate(SIRV, t, step_no):
    norm_error = np.sum(SIRV[step_no]) - np.sum(SIRV_initial)    
    epsilon = 1e-6
    if norm_error > epsilon:
        print 'Error: Equality condition broken at step=%d with error %f' %(step_no, norm_error)
        return True
    else:
        """ Everything is okaaaaay"""
        return False
        
def SIRV_visualize(t, SIRV):
    plt.figure('SIRV')
    plt.plot(t, SIRV)
    plt.legend(['Susceptibles', 'Infected', 'Recovered', 'Vaccinated'])
    plt.show()

if __name__ == '__main__':
    main()
"""Output:
SIRV modelling
Condition at last day=60: S=2, I=2, R=157, V=1341
Maximum number of infected = 64

We see that the vaccination is effective and reduces the maximum number of 
infected.
""" 