# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:16:39 2015

@author: Camilla Nore
"""
"""
E.44 (SIRV_varying_p.py, side 786, 2 poeng)

Let the vaccination campaign in E.43 start 6 days after the
outbreak of the disease and let it last for 10 days,
p(t) = 0.1, 6 ≤ t ≤ 15,
0, otherwise.
"""

import ODESolver
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Example:
    problem = ProblemSIRV(beta=0.0005,
                          nu=0.1, S0=1500, I0=1, R0=0, V0=0, T=60, 
                          p = vaccination_rate)
    solver = SolverSIRV(problem, 0.5)
    #print solver.dt  
    solver.solve()
    solver.plot()
    #print beta(0)
    #print beta(13)
    #print solver.SIRV[:,1].max()
    

def vaccination_rate(t):
    if 6 <= t <= 15:
        p = 0.1
        return p
    else:
        p = 0.0
        return p
        
def beta(t):
    if t <= 12:
        beta = 0.0005
        return beta
    else:
        beta = 0.0001
        return beta
        
class ProblemSIRV:
    def __init__(self, nu, beta, S0, I0, R0, V0, T, p=0.0): 
        
        """
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulation for t in [0,T]
        """
        if isinstance(nu, (float,int)): # number?
            self.nu = lambda t: nu # wrap as function
        elif callable(nu):
            self.nu = nu
        # same for beta and self.beta
        if isinstance(beta, (float,int)): # number?
            self.beta = lambda t: beta # wrap as function
        elif callable(beta):
            self.beta = beta
        # p vaccitation rate is time varying
        if isinstance(p, (float,int)): # number?
            self.p = lambda t: p # wrap as function
        elif callable(p):
            self.p = p
    
        self.SIRV_initial = np.asarray([S0, I0, R0, V0])
        self.T = T
    # store the other parameters

    def __call__(self, SIRV, t):
        """Right-hand side function of the ODE system."""
        return self.SIRV_timederivative(SIRV, t)

    def SIRV_timederivative(self, SIRV, t):
        """Return the SIR d/dt values for the given input data [S, I, R]."""  
        beta = self.beta(t)
        nu = self.nu(t)
        p = self.p(t)
        Sddt = - beta*SIRV[0]*SIRV[1] - p*SIRV[0]
        Iddt =   beta*SIRV[0]*SIRV[1] - nu*SIRV[1]
        Rddt =                        nu*SIRV[1]
        Vddt =                        p*SIRV[0]
        return [Sddt, Iddt, Rddt, Vddt]
    
    def SIRV_validate(self, SIRV, t, step_no):
        norm_error = np.sum(SIRV[step_no]) - np.sum(self.SIRV_initial)    
        epsilon = 1e-6
        if norm_error > epsilon:
            print 'Error: Equality condition broken at step=%d with error %f' %(step_no, norm_error)
            return True
        else:
            """ Everything is okaaaaay"""
            return False

class SolverSIRV:
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=ODESolver.RungeKutta4):    
        """ Solve the SIR system, and return a numpy array with t, S, I and R."""
        self.solver = method(self.problem)
        self.solver.set_initial_condition(self.problem.SIRV_initial)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        self.SIRV, self.t = self.solver.solve(t, terminate = self.problem.SIRV_validate)
        # TODO: SIR validate as terminate function

    def plot(self):
    # plot S(t), I(t), and R(t)
        plt.figure('SIRV')
        plt.plot(self.t, self.SIRV)
        plt.legend(['Susceptibles', 'Infected', 'Recovered', 'Vaccinated'])
        plt.show()

if __name__ == '__main__':
    main()

"""Output:
See graph.
"""