# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 08:13:36 2015

@author: Camilla Nore
"""


""" 
Exercise E.9: Verify the limit as time grows

a) Compute the limit by hand

rho   - fluid density
rho_b - body density
v     - velocity
g     - gravity 9.81 m/ss
Cd    - drag coefficient
A     - Cross section area
V     - volume of body

-  We ignore the sign of v_term , |v|v = v^2
-  At terminal velocity, v_term, dv/dt = 0
-> v_term = sqrt[ 2gV(rho_b/rho - 1)/(A*Cd) ]

"""

import ODESolver
import math
import matplotlib.pyplot as plt
import numpy as np


class FallingBody:
    def __init__(self, rho, rho_b, Cd, A, V, v0):
        self.rho = rho      # Fluid density           kg/m^3
        self.rho_b = rho_b  # Body density            kg/m^3
        self.Cd = Cd        # Drag coefficient        -
        self.A = A          # Cross-section area      m^2
        self.V = V          # Volume of body          m^3
        self.v0 = v0        # Initial velocity, t=0   m/s
        self.g = 9.81       # Gravity                 m/s^2
        self.v = None       # The solution
        self.t = None       # The timevector of the solution

    def __call__(self, v, t):
        """ dv/dt - velocity time derivative. (E.63) """
        dvdt = (- self.g * (1 - self.rho/self.rho_b)
                - 0.5*self.Cd*self.rho*self.A/(self.rho_b*self.V)*np.abs(v)*v)
        if math.isnan(dvdt):
            raise ValueError('Time derivative resulted in Nan-value')
        return dvdt

    def stop_at_terminal_velocity(self, v_vector, t, step_no, eps=1e-5):
        """ Compare this and the previos time step. If no change - stop """
        diff = np.abs(v_vector[step_no]-v_vector[step_no-1])
        if diff < eps:
            return True
        else:
            return False

    def analytical_term_velocity(self):
        """ v_term = sqrt[ 2gV(rho_b/rho - 1)/(A*Cd) ] """
        v_term2 = 2*self.g*self.V*(self.rho_b/self.rho-1)/(self.A*self.Cd)
        v_term = math.sqrt(np.abs(v_term2))
        if self.rho_b > self.rho:
            # If the body is more dense than the fluid, it falls down.
            v_term *= -1
        return v_term

    def plot(self, name, dt=''):
        if self.v is not None and self.t is not None:
            plt.figure(name)
            plt.plot(self.t, self.v, label=name+' dt:'+str(dt))
            plt.plot((0.0, self.t[-1]),
                     np.ones(2)*self.analytical_term_velocity(), '--')
            plt.legend(loc='best')
            plt.title(name)
            plt.xlabel('Time [s]')
            plt.ylabel('Velocity [m/s]')


def plot_v_term_error(dt_values, v_term, v_term_true, name):
    """ c) Graph the terminal velocity as a function of dt. """
    plt.figure('Terminal velocity:'+name)
    plt.title('Terminal velocity:'+name)
    plt.plot(dt_values, v_term, 'o-', label=name+'v_term')
    plt.plot(dt_values, np.ones(len(dt_values))*v_term_true,
             '--', label='Analytical v_term')
    plt.xlabel('dt [s]')
    plt.xscale('log')
    plt.grid()
    plt.ylabel('v_term [m/s]')


def main():
    # Create the two problems.
    skydiver = FallingBody(rho = 0.79, rho_b = 1003.0, V = 0.08, A = 0.9,
                           Cd = 0.6, v0 = 0.0)
    ball_radius  = 0.11
    ball_volume  = 4/3.0*math.pi*ball_radius**3
    ball_cs_area = math.pi*ball_radius**2
    ball_mass_kg = 0.43 
    ball_density = ball_mass_kg/ball_volume
    ball_in_water = FallingBody(rho = 1000.0, rho_b = ball_density,
                                Cd = 0.2, A = ball_cs_area, V = ball_volume,
                                v0 = 0.0)

    # Run the solvers with different timesteps.
    T = 80  # maximum time in seconds
    dt_skydiver = [5, 3, 1, 1e-1, 1e-2, 1e-3]
    dt_ball = [0.03, 0.02, 1e-2, 1e-3]
    # For loop on Problem        dt values    name
    problems = ((skydiver,      dt_skydiver, 'Skydiver'), 
                (ball_in_water, dt_ball,     'Ball in water'))
    for prob, dt_values, name in problems:
        solver = ODESolver.RungeKutta4(prob)
        solver.set_initial_condition(prob.v0)
        v_term = []
        for dt in dt_values:
            t = np.linspace(0, T, T/dt)
            try:
                prob.v, prob.t = solver.solve(t, prob.stop_at_terminal_velocity)
                # prob.v, prob.t = solver.solve(t)  # Note 1.
                v_term.append(prob.v[-1])
                prob.plot(name, dt)
            except ValueError, e:
                print 'Error for dt=%f:' % (dt), e
                v_term.append(np.NaN)
        plot_v_term_error(dt_values, v_term, prob.analytical_term_velocity(), name)

    # Show all the plot windows.
    plt.show()


if __name__ == '__main__':
    main()


""" Output:

The program creates 4 plots.

Note 1:

The terminal velocity plots indicate that the error increase as we use smaller
dt values. This is a result of using the terminate condition.

If we disable the terminal condition, and run the simulation up to t = T, we get
decreasing deviation as we decrease dt, as expected.

This was _not_ evident to me :)
"""