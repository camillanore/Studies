# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:03:11 2015

@author: NBCNO1
"""
"""
E.6 (tank_ODE.py, side 766)
"""
import math
import numpy as np
import matplotlib.pyplot as plt

gravity_mss = 9.81 # meter/ second^2

def delta_h(r_m, R_m, h_m, dt_s):
    return -(r_m / R_m)**2 * math.sqrt(2*gravity_mss*h_m) *dt_s
    # Double check units: m/m *sqrt(mm/ss)*s = m    
    
def analytical_h(r_m, R_m, h0,t_s):
    return math.exp(-(r_m/R_m)**2*math.sqrt(2*gravity_mss)*t_s)
    
def euler_integrate(r_m, R_m, h0):
    dt_s = 0.01
    h_list = [h0]
    h_current = h0
    while h_current > 0:
        h_next = h_current + delta_h(r_m, R_m, h_current, dt_s)
        h_list.append(h_next)
        h_current = h_next

    h_list = np.asarray(h_list)
    time = np.linspace(0.0, dt_s*len(h_list), num = len(h_list))
    return h_list, time

def plot_ht(t_values,h_values):
    plt.figure()
    for h in h_values:
        plt.plot(t_values, h)
    plt.xlabel('Time [s]')
    plt.ylabel('Fluid height [m]')
    plt.show()
    
if __name__ == '__main__':
    r_m = 0.01 #m
    R_m = 0.20 #m
    h0 = 1.0   #m    
    height, time = euler_integrate(r_m, R_m, h0)
    analytical = [analytical_h(r_m,R_m,h0,t) for t in time]
    plot_ht(time, [height, analytical])
    print 'The tank is empty after %g seconds' %(time[-1])

"""Output:
The tank is empty after 180.57 seconds.
I do not believe the analytical answer is correct. 
"""