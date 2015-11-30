# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:04:58 2015

@author: Camilla Nore

E.45 (SIRV_optimal_duration.py, side 786, 2 poeng)

Let the vaccination campaign in Exercise E.44 last for VT days:
p(t) = 0.1, 6 ≤ t ≤ 6 + VT ,
0, otherwise

Compute the maximum number of infected people, maxt I(t), as a function
of VT ∈ [0, 31], by running the model for VT = 0, 1, 2 . . . , 31. Plot this
function. Determine from the plot the optimal VT , i.e., the smallest vaccination
period VT such that increasing VT has negligible effect on the maximum
number of infected people. 
"""

import ODESolver
import numpy as np
import matplotlib.pyplot as plt

VT = 0

def main():
    # Example:
    vt_vector = range(0,32)
    max_inf = np.zeros(len(vt_vector))
    
    for i, vt in enumerate(vt_vector):
        vaccination_rate_vt = lambda t: 0.1 if t > 6 and t < (6 + vt) else 0.0
        problem = ProblemSIRV(beta=0.0005,
                          nu=0.1, S0=1500, I0=1, R0=0, V0=0, T=60, 
                          p = vaccination_rate_vt)
        solver = SolverSIRV(problem, 0.5)
        solver.solve()
        max_inf[i] = solver.SIRV[:,1].max()
        print 'max infected=%.1f when VT=%d' %(solver.SIRV[:,1].max(), vt)
        solver.plot()
    
    change_in_max_inf = max_inf[:-1] - max_inf[1:]    
    vt_stop = np.where(change_in_max_inf <=1)[0][0]
    print 'The vaccination has no effect after vt =%.f' %vt_stop
    plt.figure('vt')
    plt.plot(vt_vector, max_inf)
    plt.xlabel('Duration of vaccination period [days]')
    plt.ylabel('Number of infected')
    plt.title('What is the optimal duration of vaccination?')
def vaccination_rate(t):
    if 6 <= t <= (6 + VT):
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
max infected=897.9 when VT=0
max infected=800.3 when VT=1
max infected=700.0 when VT=2
max infected=618.9 when VT=3
max infected=555.7 when VT=4
max infected=510.3 when VT=5
max infected=480.1 when VT=6
max infected=463.4 when VT=7
max infected=456.6 when VT=8
max infected=455.8 when VT=9
max infected=455.8 when VT=10
max infected=455.8 when VT=11
max infected=455.8 when VT=12
max infected=455.8 when VT=13
max infected=455.8 when VT=14
max infected=455.8 when VT=15
max infected=455.8 when VT=16
max infected=455.8 when VT=17
max infected=455.8 when VT=18
max infected=455.8 when VT=19
max infected=455.8 when VT=20
max infected=455.8 when VT=21
max infected=455.8 when VT=22
max infected=455.8 when VT=23
max infected=455.8 when VT=24
max infected=455.8 when VT=25
max infected=455.8 when VT=26
max infected=455.8 when VT=27
max infected=455.8 when VT=28
max infected=455.8 when VT=29
max infected=455.8 when VT=30
max infected=455.8 when VT=31
The vaccination has no effect after vt =8

Stabilizes when VT =8. Therefore I choose to stop the vaccination period after 
VT =8, i.e. t = 6 + 8 = 14 days. 
"""