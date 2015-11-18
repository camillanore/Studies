# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:19:30 2015

@author: NBCNO1
"""
"""
E.30 (RungeKutta2_func.py, side 778), 

Exercise E.30: Implement a 2nd-order Runge-Kutta method;
function

Implement the 2nd-order Runge-Kutta method specified in formula (E.38).
Use a plain function RungeKutta2 of the type shown in Section E.1.2 for
the Forward Euler method. Construct a test problem where you know the
analytical solution, and plot the difference between the numerical and
analytical solution. Demonstrate that the numerical solution approaches
the exact solution as Δt is reduced. Filename: RungeKutta2_func.py

"""
import numpy as np

class ODESolver:
    """
    Superclass for numerical methods solving scalar and vector ODEs

      du/dt = f(u, t)

    Attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    """
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        # For ODE systems, f will often return a list, but
        # arithmetic operations with f in numerical methods
        # require that f is an array. Let self.f be a function
        # that first calls f(u,t) and then ensures that the
        # result is an array of floats.
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError

    def set_initial_condition(self, U0):
        if isinstance(U0, (float,int)):  # scalar ODE
            self.neq = 1
            U0 = float(U0)
        else:                            # system of ODEs
            U0 = np.asarray(U0)          # (assume U0 is sequence)
            self.neq = U0.size
        self.U0 = U0

        # Check that f returns correct length:
        try:
            f0 = self.f(self.U0, 0)
        except IndexError:
            raise IndexError('Index of u out of bounds in f(u,t) func. Legal indices are %s' % (str(range(self.neq))))
        if f0.size != self.neq:
            raise ValueError('f(u,t) returns %d components, while u has %d components' % (f0.size, self.neq))

    def solve(self, time_points, terminate=None):
        """
        Compute solution u for t values in the list/array
        time_points, as long as terminate(u,t,step_no) is False.
        terminate(u,t,step_no) is a user-given function
        returning True or False. By default, a terminate
        function which always returns False is used.
        """
        if terminate is None:
            terminate = lambda u, t, step_no: False

        if isinstance(time_points, (float,int)):
            raise TypeError('solve: time_points is not a sequence')
        if time_points.size <= 1:
            raise ValueError('ODESolver.solve requires time_points array with at least 2 time points')

        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1:  # scalar ODEs
            self.u = np.zeros(n)
        else:              # systems of ODEs
            self.u = np.zeros((n,self.neq))

        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        # Time loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break  # terminate loop over k
        return self.u[:k+2], self.t[:k+2]
        
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
        
class RungeKutta2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)      
        u_new = u[k] + K2
        return u_new

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

#RK2
rk2 = RungeKutta2(f)
rk2.set_initial_condition(1.0)
urk2, trk2 = rk2.solve(t)


# Compare numerical solution and exact solution in a plot

import matplotlib.pyplot as plt 
import math

print np.exp(t)
print urk2
print trk2
u_exact = np.exp(t)
plt.figure('rk2')
plt.plot(t, u, 'r-', t, u_exact, 'b-', trk2, urk2, 'm-')
plt.xlabel='t' 
plt.ylabel='u'
plt.legend=(['numerical', 'exact', 'rk2'])
plt.legend()
plt.title="Solution of the ODE u'=u, u(0)=1"
plt.show()
#plt.savefig='tmp.pdf'


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
