# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:25:23 2015

@author: Camilla Nore

Exercise E.7: Solve an ODE for the arc length
"""

import ODESolver # From book examples folder
import numpy as np
import matplotlib.pyplot as plt

def dsdx(y, t=0.0):
    return np.sqrt(1.0 + dfdx**2)
    
def main():
    x = np.linspace(0,2)
    f_x = 0.5*x + 1
    df_xdx = 0.5
    f_x_parabola = x**2
    df_x_paraboladx = 2*x
   
    eul_obj = ODESolver.ForwardEuler(dfdx)   
    eul_obj.set_initial_condition(x0)
    
    
    # Start plot    
    plt.figure('ODE')
    plt.title('Forward Euler')
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
