# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:15:19 2015

@author: NBCNO1
"""
"""
Obligatoriske innleveringsoppgaver: 
E.41 (SIR.py, side 782, 2 poeng), 

E.42 (SIR_class.py, side 784, 2 poeng), 
E.43 (SIRV.py, side 785, 2 poeng), 
E.44 (SIRV_varying_p.py, side 786, 2 poeng), 
E.45 (SIRV_optimal_duration.py, side 786, 2 poeng), 
E.46 (SIZR.py, side 786, 2 poeng), 
E.47 (Night_of_the_Living_Dead.py, side 789, 2 poeng), 
E.48 (war_on_zombies.py, side 789, 4 poeng)
"""

"""
Exercise E.41: Simulate the spreading of a disease by a SIR
model

Make a function for solving the differential equations in the SIR model
by any numerical method of your choice. Make a separate function for
visualizing S(t), I(t), and R(t) in the same plot.
Visualizing S(t), I(t), and R(t) in the same plot.

Adding the equations shows that S' + I' + R' = 0, which means that
S +I +R must be constant. Perform a test at each time level for checking
that S + I + R equals S0 + I0 + R0 within some small tolerance. If a
subclass of ODESolver is used to solve the ODE system, the test can be
implemented as a user-specified terminate function that is called by the
solve method a every time level (simply return True for termination if
S + I + R is not sufficiently constant).

A specific population has 1500 susceptibles and one infected. We are
interested in how the disease develops. Set S(0) = 1500, I(0) = 1, and
R(0) = 0. Choose ν = 0.1, Δt = 0.5, and t ∈ [0, 60]. Time t here
counts days. Visualize first how the disease develops when β = 0.0005.
Certain precautions, like staying inside, will reduce β. Try β = 0.0001
and comment from the plot how a reduction in β influences S(t). (Put
the comment as a multi-line string in the bottom of the program file.)

Filename: SIR.py
"""
import numpy as np
import matplotlib.pyplot as plt

# Time unit: 1 h
beta = 0.0005 #then try beta = 0.0001
nu = 0.1
print 'beta:', beta, 'nu:', nu

dt = 0.5             # 30 min (?)
D = 30               # simulate for D days
N = int(D*24/dt)     # corresponding no of hours


t = np.linspace(0, N*dt, N+1)
S = np.zeros(N+1)
I = np.zeros(N+1)
R = np.zeros(N+1)

# Initial condition
S[0] = 1500
I[0] = 1
R[0] = 0

# Step equations forward in time
for n in range(N):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*nu*I[n]
    R[n+1] = R[n] + dt*nu*I[n]

plt.plot(t, S, 'k-', t, I, 'b-', t, R, 'r-')
plt.legend(['S', 'I', 'R'], loc='lower right')
plt.xlabel('hours')
plt.savefig('tmp.pdf')
plt.savefig('tmp.png')

print S[:4], I[:4], R[:4]
plt.show()