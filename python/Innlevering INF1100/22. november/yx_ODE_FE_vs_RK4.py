# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:31:45 2015

@author: Camilla Nore
"""

"""
E.23 (yx_ODE_FE_vs_RK4.py, side 775, 2 poeng),
 
Exercise E.23: Compare ODE methods

Investigate the accuracy of the 4th-order Runge-Kutta method and the
Forward Euler scheme for solving the (challenging) ODE problem:

dy/dt = 1/(2*(y-1))
y(0) = 1 + math.sqrt(epsilon)
x = range (0,1,4) # start, step,stop

where epsilon is a small number, say epsilon = 0.001. 

Start with four steps in [0, 4] and reduce the step size repeatedly by a factor
of two until you find thesolutions sufficiently accurate. 
Make a plot of the numerical solutions
along with the exact solution 
y(x) = 1 + math.sqrt(x + epsilon) for each step size.

Filename: yx_ODE_FE_vs_RK4.py.
"""
import ODESolver # From book examples folder
import numpy as np
import matplotlib.pyplot as plt

def dydx(y, t=0.0):
    return 1.0/(2*(y-1))
    
def main():
    epsilon = 0.001
    y0 = 1 + np.sqrt(epsilon)
    #TODO: start with four steps, double until sufficient accurate.
    rk4_obj = ODESolver.RungeKutta4(dydx)
    eul_obj = ODESolver.ForwardEuler(dydx)
    rk4_obj.set_initial_condition(y0)    
    eul_obj.set_initial_condition(y0)
    
    # Exact solution    
    x = np.linspace(0,4)
    y_exact = 1 + np.sqrt(x + epsilon)
    
    # Start plot    
    plt.figure('ODE')
    plt.title('Forward Euler and RK4 compared')
    plt.plot(x, y_exact, '--', label= 'Exact solution')
    
    N = 4
    rk4_error = np.inf
    print 'N\trk4 err\t eul err'
    print '--------------------'
    while (rk4_error > 1e-1):
        x_values = np.linspace(0,4,N)
        y_rk4, x_rk4 = rk4_obj.solve(x_values)
        y_eul, x_eul = eul_obj.solve(x_values)
        
        rk4_error = np.abs(y_rk4[-1] - y_exact[-1])
        eul_error = np.abs(y_eul[-1] - y_exact[-1])
        print '%d\t%f\t%f' %(N, rk4_error, eul_error)
        plt.plot(x_rk4, y_rk4, 'g-', label= 'RungeKutta4 solution')
        plt.plot(x_eul, y_eul, 'r-', label= 'ForwardEuler solution')
        N = N*2
    
    #TODO: plot numerical along with exact
           
    plt.legend(['Exact', 'RK4', 'Euler'], loc='best')
    plt.show()  

if __name__ == '__main__':
    main()
print ODESolver
"""Output:
N	rk4 err	 eul err
--------------------
4	5.280915	19.176328
8	1.593435	7.253912
16	0.429609	2.667875
32	0.104404	0.860566
64	0.023899	0.243306

"""