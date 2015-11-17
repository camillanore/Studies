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