# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:46:20 2015

@author: Camilla Nore
"""
import pylab
import numpy as np



# Exercise 1.11: Compute the air resistance on a football

def air_resistance(velocity,           #m/s
                   radius=0.11,         #m
                   drag_coefficient=0.2):   #no units
                    
    k_air_density = 1.2 # kg/m**3 
    area = np.pi*radius**2
    drag_force = (0.5*drag_coefficient*k_air_density*
                        area*velocity**2)
    return drag_force # N
   
air_drag=[]
velocity=[]
for i in range(0,400):
    velocity.append(i/10.0)
    air_drag.append(air_resistance(i/10.0))
pylab.plot(velocity,air_drag)
pylab.xlabel('Velocity, m/s')
pylab.ylabel('Drag force, N')

def convert_kmh_to_ms( vel_kmh):
   return vel_kmh/3.6 # m/s
   
# Requested output:
# Forces for V = 120 km/h: Drag = 13.9 N,  Gravity = 3.2 N, Ratio = 10.1
def print_forces(vel_kmh, mass=0.43):
    vel=convert_kmh_to_ms(vel_kmh)
    drag=air_resistance(vel)
    gravity_force=9.81*mass
    ratio=gravity_force/drag
    print ''.join( #join empty string with list of strings.
    ('Forces for V = ', format(vel,'.1f'), 
    ' km/h: Drag = ', format(drag,'.1f'), 
    ' N, Gravity = ', format(gravity_force,'.1f'), 
    ' N, Ratio = ', format(ratio,'.1f'), '.'))
    
print_forces(120)

print_forces(10)