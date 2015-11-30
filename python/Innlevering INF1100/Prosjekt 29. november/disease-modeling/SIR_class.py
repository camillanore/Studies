# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:18:11 2015

@author: Camilla Nore

E.42 (SIR_class.py, side 784, 2 poeng)

Now we shall make an implementation of
the f(u, t) function specifying the ODE system such that ν and β can
be given as either a constant or a Python function. Introduce a class for
f(u, t). 

Write the complete code for class ProblemSIR based on the sketch of
ideas above. The ν parameter is usually not varying with time as 1/ν
is a characteristic size of the period a person is sick, but introduction
of new medicine during the disease might change the picture such that
time dependence becomes relevant.

After the breakout of a disease, authorities often start campaigns for
decreasing the spreading of the disease. Suppose a massive campaign
telling people to wash their hands more frequently is launched, with the
effect that β is significantly reduced after a some days. For the specific
case simulated in Exercise E.41, let:

β(t) =     0.0005, 0 ≤ t ≤ 12,
           0.0001, t > 12

Simulate this scenario with the Problem and Solver classes. Report the
maximum number of infected people and compare it to the case where
β(t) = 0.0005. Filename: SIR_class.py.
"""
import ODESolver
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Example:
    problem = ProblemSIR(beta=beta,
    nu=0.1, S0=1500, I0=1, R0=0, T=60)
    solver = SolverSIR(problem, 0.5)  
    solver.solve()
    print 'Maximum number of infected:%d' % solver.SIR[:,1].max()    
    solver.plot()
    #print beta(0)
    #print beta(13)
    
def beta(t):
    if t <= 12:
        beta = 0.0005
        return beta
    else:
        beta = 0.0001
        return beta
        
class ProblemSIR:
    def __init__(self, nu, beta, S0, I0, R0, T): 
        
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
        self.SIR_initial = np.asarray([S0, I0, R0])
        self.T = T
    # store the other parameters

    def __call__(self, SIR, t):
        """Right-hand side function of the ODE system."""
        return self.SIR_timederivative(SIR, t)

    def SIR_timederivative(self, SIR, t):
        """Return the SIR d/dt values for the given input data [S, I, R]."""  
        beta = self.beta(t)
        nu = self.nu(t)
        Sddt = - beta*SIR[0]*SIR[1]
        Iddt =   beta*SIR[0]*SIR[1] - nu*SIR[1]
        Rddt =                        nu*SIR[1]
        return [Sddt, Iddt, Rddt]
    
    def SIR_validate(self, SIR, t, step_no):
        norm_error = np.sum(SIR[step_no]) - np.sum(self.SIR_initial)    
        epsilon = 1e-6
        if norm_error > epsilon:
            print 'Error: Equality condition broken at step=%d with error %f' %(step_no, norm_error)
            return True
        else:
            """ Everything is okaaaaay"""
            return False

class SolverSIR:
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=ODESolver.RungeKutta4):    
        """ Solve the SIR system, and return a numpy array with t, S, I and R."""
        self.solver = method(self.problem)
        self.solver.set_initial_condition(self.problem.SIR_initial)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        self.SIR, self.t = self.solver.solve(t)
        # TODO: SIR validate as terminate function

    def plot(self):
    # plot S(t), I(t), and R(t)
        plt.figure('SIR')
        plt.plot(self.t, self.SIR)
        plt.legend(['Susceptibles', 'Infected', 'Recovered'])
        plt.show()

if __name__ == '__main__':
    main()
    
"""Output:
For beta=0.0005 (to compare)
Maximum number of infected:897

For beta = beta (this exercise)
Maximum number of infected:745

"""