# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:11:53 2015

@author: Camilla Nore

E.46 (SIZR.py, side 786, 2 poeng)
"""

import ODESolver
import numpy as np
import matplotlib.pyplot as plt

VT = 0

def main():
    # Example:
    problem = ProblemSIZR(beta=0.0012, alfa=0.0016, delta_I=0.014, delta_s=0.0, 
                          sigma=2.0, ro=1.0, T=24,
                          SIZR_initial=[10, 100, 0, 0])

    solver = SolverSIZR(problem, 0.5)
    solver.solve()   
    solver.plot()
       
def beta(t):
    if t <= 12:
        beta = 0.0005
        return beta
    else:
        beta = 0.0001
        return beta
        
class ProblemSIZR:
    def __init__(self, beta, sigma, ro, delta_s, delta_I, alfa, SIZR_initial, T):         
        """
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulation for t in [0,T]
        """

        # same for beta and self.beta
        if isinstance(beta, (float,int)): # number?
            self.beta = lambda t: beta # wrap as function
        elif callable(beta):
            self.beta = beta
        # p vaccitation rate is time varying
        if isinstance(sigma, (float,int)): # number?
            self.sigma = lambda t: sigma # wrap as function
        elif callable(sigma):
            self.sigma = sigma
        if isinstance(delta_s, (float,int)): # number?
            self.delta_s = lambda t: delta_s # wrap as function
        elif callable(delta_s):
            self.delta_s = delta_s
        if isinstance(delta_I, (float,int)): # number?
            self.delta_I = lambda t: delta_I # wrap as function
        elif callable(delta_I):
            self.delta_I = delta_I
        if isinstance(alfa, (float,int)): # number?
            self.alfa = lambda t: alfa # wrap as function
        elif callable(alfa):
            self.alfa = alfa
        if isinstance(ro, (float,int)): # number?
            self.ro = lambda t: ro # wrap as function
        elif callable(ro):
            self.ro = ro

        self.SIZR_initial = np.asarray(SIZR_initial)
        self.T = T    # store the other parameters

    def __call__(self, SIZR, t):
        """Right-hand side function of the ODE system."""
        return self.SIZR_timederivative(SIZR, t)

    def SIZR_timederivative(self, SIZR, t):
        """Return the SIR d/dt values for the given input data [S, I, R]."""  
        beta = self.beta(t)
        sigma = self.sigma(t)
        delta_s = self.delta_s(t)
        ro = self.ro(t)
        delta_I = self.delta_I(t)
        alfa = self.alfa(t)
        
        Sddt = sigma- beta*SIZR[0]*SIZR[2] - delta_s*SIZR[0]
        Iddt =        beta*SIZR[0]*SIZR[2] - ro*SIZR[1]     - delta_I*SIZR[1]
        Zddt =                               ro*SIZR[1]                       - alfa*SIZR[0]*SIZR[2]
        Vddt =                              delta_s*SIZR[0] + delta_I*SIZR[1] + alfa*SIZR[0]*SIZR[2]
        return [Sddt, Iddt, Zddt, Vddt]
    
    def SIZR_validate(self, SIZR, t, step_no):
        norm_error = np.sum(SIZR[step_no]) - np.sum(self.SIZR_initial)    
        epsilon = 1e-6
        if norm_error > epsilon:
            print 'Error: Equality condition broken at step=%d with error %f' %(step_no, norm_error)
            return True
        else:
            """ Everything is okaaaaay"""
            return False

class SolverSIZR:
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=ODESolver.RungeKutta4):    
        """ Solve the SIR system, and return a numpy array with t, S, I and R."""
        self.solver = method(self.problem)
        self.solver.set_initial_condition(self.problem.SIZR_initial)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        self.SIZR, self.t = self.solver.solve(t)
        # TODO: SIR validate as terminate function

    def plot(self):
    # plot S(t), I(t), and R(t)
        plt.figure('SIZR')
        plt.plot(self.t, self.SIZR)
        plt.legend(['Susceptibles', 'Infected', 'Zombies', 'Removed'])
        plt.xlabel('Hours')
        plt.show()

if __name__ == '__main__':
    main()

"""Output:
See graph.
"""