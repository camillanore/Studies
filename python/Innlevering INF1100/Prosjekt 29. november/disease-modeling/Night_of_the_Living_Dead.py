# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:36:07 2015

@author: Camilla Nore
"""

"""
E.47 (Night_of_the_Living_Dead.py, side 789, 2 poeng), 
"""

import ODESolver
import numpy as np
import matplotlib.pyplot as plt

VT = 0

def main():
    # Example:
    params = SIZR_parameters(time_phases = [4.0,28.0, 33.0],
                             betas =       [0.03, 0.0012, 0.0],
                             alphas =      [0.0,0.0016,0.006],
                             sigmas =      [20.0, 2.0, 0.0],                            
                             deltaIs=      [0.0, 0.014, 0.0],
                             deltass =     [0.0, 0.0, 0.0067])
                      
    problem = ProblemSIZR(beta=params.beta, 
                          alfa = params.alpha, 
                          delta_I = params.deltaI, 
                          delta_s=params.deltas, 
                          sigma=params.sigma, 
                          ro=1.0, 
                          T=35,
                          SIZR_initial=[60, 0, 1, 0])
    solver = SolverSIZR(problem, 0.5)
    solver.solve()   
    solver.plot()

class SIZR_parameters():
    """ I chose to assign the parameters as a class implemetation instead of 
        piecewise function."""
    def __init__(self, time_phases, betas, alphas, sigmas, deltaIs, deltass):
        n = len(time_phases)
        assert n == len(betas)        
        assert n == len(alphas)
        assert n == len(sigmas)
        assert n == len(deltaIs)
        assert n == len(deltass)
        self.time_phases = time_phases
        self.betas = betas        
        self.alphas = alphas
        self.sigmas = sigmas
        self.deltaIs = deltaIs
        self.deltass = deltass
    def get_index(self, t):
        """Assume that the time phases are in increasing order.
           If t> last_time_phase, the last value will be returned."""        
        for i, t_limit in enumerate(self.time_phases):
            if t < t_limit:
                break                
        return i
    def beta(self, t):
        return self.betas[self.get_index(t)]
    def alpha(self, t):
        return self.alphas[self.get_index(t)]
    def sigma(self, t):
        return self.sigmas[self.get_index(t)]
    def deltaI(self, t):
        return self.deltaIs[self.get_index(t)]
    def deltas(self, t):
        return self.deltass[self.get_index(t)]
        
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
        plt.legend(['Susceptibles', 'Infected', 'Zombies', 'Removed'], 
                   loc='best')
        plt.xlabel('Hours')
        plt.show()

if __name__ == '__main__':
    main()

"""Output:
See graph. All the zombies are not dead after 33 hours, but the plot still
makes sence. During the counter attack phase the number of zombies are reduced.
"""