# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:36:58 2015

@author: Camilla Nore
"""
"""
E.48 (war_on_zombies.py, side 789, 4 poeng)
"""
import ODESolver
import numpy as np
import matplotlib.pyplot as plt

VT = 0

def main():
    # Example:
    problem = ProblemSIZR(beta=0.03, alfa=alfa_attack, delta_I=0.0, delta_s=0.0, 
                          sigma=2.0, ro=1.0, T=20,
                          SIZR_initial=[50, 0, 3, 0])
    
    solver = SolverSIZR(problem, 0.01) 
    solver.solve()   
    print 'SIZR vector at t = 20:', solver.SIZR[-1]
    print 'Min value of  Zombies:', solver.SIZR[:,2].min()
    solver.plot()
    
def alfa_attack(t):
    time_of_attacks = [5, 10, 18] #hours
    beta_init = 0.03
    alfa_init = 0.2*beta_init
    a =50*alfa_init
    # The attacks last for two hours
    sigma_duration = 0.5 # duration of attack is 4*sigma
    omega_elements = [np.exp(-0.5*((t-T_i)/sigma_duration)**2)
                     for T_i in time_of_attacks]
    omega = a*np.sum(omega_elements)
    return alfa_init + omega

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
                    loc = 'best')
        plt.xlabel('Hours')
        plt.show()

if __name__ == '__main__':
    main()

"""Output:
SIZR vector at t = 20: [ 24.14203701   0.79583938   1.157213    66.90491061]
Min value of  Zombies: 0.363289913935

We see that the minimum value of the zombies is 0.36, which means that there are 
no zombies left. However, as this is a numerical model with continuos variables,
the model does not capture the fact that individuals only have discrete values.
In order to model this correctly one has to use much more complicated models.
The differential models used here works well when modelling large populations,
but does not work well in borderline cases as shown here.

As the graph suggests the war on zombies does not appear to be sufficient to
save mankind. However, the graph clearly shows that the number of zombies
decline radically after the attacks. As we know that the number of zombies is 
close to zero after the war on zombies, it seems that the three attacks are
sufficient to save mankind. 
"""