# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:15:19 2015

@author: Camilla Nore
"""
"""
Exercise E.41: Simulate the spreading of a disease by a SIR
model

Make a function for solving the differential equations in the SIR model
by any numerical method of your choice. Make a separate function for
visualizing S(t), I(t), and R(t) in the same plot.

Adding the equations shows that S' + I' + R' = 0, which means that
S +I +R must be constant. Perform a test at each time level for checking
that S + I + R equals S0 + I0 + R0 within some small tolerance. If a
subclass of ODESolver is used to solve the ODE system, the test can be
implemented as a user-specified terminate function that is called by the
solve method a every time level (simply return True for termination if
S + I + R is not sufficiently constant).

A specific population has 1500 susceptibles and one infected. We are
interested in how the disease develops. Set S(0) = 1500, I(0) = 1, and
R(0) = 0. Choose ν = 0.1, Δt = 0.5, and t ∈ [0, 60]. Time t here
counts days. Visualize first how the disease develops when β = 0.0005.
Certain precautions, like staying inside, will reduce β. Try β = 0.0001
and comment from the plot how a reduction in β influences S(t). (Put
the comment as a multi-line string in the bottom of the program file.)

"""
import numpy as np
import matplotlib.pyplot as plt
import ODESolver

"""Global values for initial conditions and parameters"""

beta = 0.0005 # Infection rate per day
mu = 0.1      # Recovery rate per day
SIR_initial = (1500, 1, 0) 

def main():
    print 'SIR modelling'
    t_days, SIR = SIR_solver(beta, mu)
    SIR_visualize(t_days, SIR)
    print 'Condition at last day=%d: S=%.f, I=%.f, R=%.0f' %(
        t_days[-1], SIR[-1,0], SIR[-1,1], SIR[-1,2])
    # TODO: make a function SIR solver
    # TODO: make a function SIR_visualize

def SIR_solver(beta, mu):
    """ Solve the SIR system, and return a numpy array with t, S, I and R."""
    n_steps = 120
    t = np.linspace(0, 250, n_steps)    
    SIR = np.zeros((n_steps, 3))
    rk4_obj = ODESolver.RungeKutta4(SIR_timederivative)
    rk4_obj.set_initial_condition(SIR_initial)
    SIR, t = rk4_obj.solve(t, terminate = SIR_validate)
    return t, SIR

def SIR_timederivative(SIR, t):
    """Return the SIR d/dt values for the given input data [S, I, R]."""       
    Sddt = - beta*SIR[0]*SIR[1]
    Iddt =   beta*SIR[0]*SIR[1] - mu*SIR[1]
    Rddt =                        mu*SIR[1]
    return [Sddt, Iddt, Rddt]

def SIR_validate(SIR, t, step_no):
    norm_error = np.sum(SIR[step_no]) - np.sum(SIR_initial)    
    epsilon = 1e-6
    if norm_error > epsilon:
        print 'Error: Equality condition broken at step=%d with error %f' %(step_no, norm_error)
        return True
    else:
        """ Everything is okaaaaay"""
        return False
        
def SIR_visualize(t, SIR):
    plt.figure('SIR')
    plt.plot(t, SIR)
    plt.legend(['Susceptibles', 'Infected', 'Recovered'])
    plt.show()

if __name__ == '__main__':
    main()
    
"""Output for beta=0.0005:
SIR modelling
Condition at last day=60: S=1, I=12, R=1488

Output for beta=0.0001 and t =300:
Condition at last day=300: S=625, I=0, R=876

When the infection rate beta is reduced, the pace of spreading of the disease
goes down dramatically. The disease thus develops at a much slower pace, and
there is no epidemy. 

"""