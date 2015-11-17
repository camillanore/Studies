# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:50:31 2015

@author: NBCNO1
"""

from ODESolver import ODESolver
import numpy as np

class MidpointIter(ODESolver):
    def __init__(self, f, N=10, eps = 1e-6):
        ODESolver.__init__(self,f) 
        self.N = N #lagre som distansevariable
        self.eps = eps
    
    def set_initial_condition(self,U0): 
        ODESolver.set_initial_condition(self,U0) #kaller funksjonen
        self.v = np.zeros((self.N+1, self.neq))
         #lage array som skal holde interne iterasjonene, v er en intern aproksimasjon 
         # til løsningen
    
    def advance(self): 
        """Advance solution one time step."""
        u, f, v = self.u, self.f, self.v
        k, t, N, eps = self.k, self.t, self.N, self.eps 
        
        dt = t[k+1] - t[k]
        v[0] = u[k]
        diff = 10 # må gå inn i while løkka
        q = 0         
        #for q in range(1, N+1):
        while q < N and diff > eps:            
            q += 1
            v[q] = u[k] + 0.5*dt*(f(u[k]), t[k] + f(v[q-1], t[k+1]))
            diff = abs(v[q] - v[q-1]) if self.neq == 1 else np.abs(v[q] - v[q-1]).max()
            # sufficient for scalar ode. if v is vector
            # in a system of ode this does not work. Må ha norm av vektoren, 
            #noe som beskriver størrelsen til ODEen. 
            
        return v[q]
""" Usikker på denne testen, og om den er implementert riktig. 
"""
def test_MidpointIter_against_hand_calculations():
    def f(u, t):
        return -2*u

    dt = 1./4
    U0 = 1
    # Hand calculations
    # 1. time step:
    U0 = 1
    t0 = 0
    u0 = U0
    v0 = U0
    t1 = dt
    v1 = u0 + 0.5*dt*(f(v0, t1) + f(u0, t0))
    v2 = u0 + 0.5*dt*(f(v1, t1) + f(u0, t0))
    u1 = v2

    # 2. time step:
    t2 = t1 + dt
    v0 = u1
    v1 = u1 + 0.5*dt*(f(v0, t2) + f(u1, t1))
    v2 = u1 + 0.5*dt*(f(v1, t2) + f(u1, t1))
    u2 = v2

    exact_u_2 = u2
    N = 2
    T = 2*dt
    n = 2
    solver = MidpointIter(f, N)
    solver.set_initial_condition(U0)
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)
    computed_u_2 = u[2]
    tol = 1E-14
    success = abs(exact_u_2 - computed_u_2) < tol
    #print 'success:', success
    assert success

if __name__ == '__main__':
    test_MidpointIter_against_hand_calculations()