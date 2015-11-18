# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:19:30 2015

@author: NBCNO1
"""
"""
E.30 (RungeKutta2_func.py, side 778), 
9.2 (Cubic_Poly4.py, side 592), 
9.11 (Backward2.py, side 595), 
E.23 (yx_ODE_FE_vs_RK4.py, side 775, 2 poeng), 
E.16 (radioactive_decay.py, side 773, 2 poeng)

Exercise E.30: Implement a 2nd-order Runge-Kutta method;
function

Implement the 2nd-order Runge-Kutta method specified in formula (E.38).
Use a plain function RungeKutta2 of the type shown in Section E.1.2 for
the Forward Euler method. Construct a test problem where you know the
analytical solution, and plot the difference between the numerical and
analytical solution. Demonstrate that the numerical solution approaches
the exact solution as Δt is reduced. Filename: RungeKutta2_func.py

"""
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
        
class RungeKutta4(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t[k] + dt2)
        K4 = dt*f(u[k] + K3, t[k] + dt)
        u_new = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return u_new
        
"""Function implementing the Forward Euler method for scalar ODEs."""
import numpy as np

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
    return u

u, t = ForwardEuler(f, U0=1, T=4, n=20)

# Compare numerical solution and exact solution in a plot

import matplotlib.pyplot as plt 
import math
u_exact = math.exp(t)
plt.plot(t, u, 'r-', t, u_exact, 'b-')
plt.xlabel='t' 
plt.ylabel='u'
plt.legend=('numerical', 'exact')
plt.title="Solution of the ODE u'=u, u(0)=1"
plt.savefig='tmp.pdf'

# More exact verification

def test_ForwardEuler_against_hand_calculations():
    """Verify ForwardEuler against hand calc. for 3 time steps."""
    u, t = ForwardEuler(f, U0=1, T=0.2, n=2)
    exact = np.array([1, 1.1, 1.21])  # hand calculations
    error = np.abs(exact - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

def test_ForwardEuler_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    def f(u, t):
        return 0.2 + (u - u_exact(t))**4

    def u_exact(t):
        return 0.2*t + 3

    u, t = ForwardEuler(f, U0=u_exact(0), T=3, n=5)
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

test_ForwardEuler_against_hand_calculations()
test_ForwardEuler_against_linear_solution()
