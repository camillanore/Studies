# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:14:39 2015

@author: NBCNO1
"""

class BungeeJump():
    def __init__(self, bungee_length_m, spring_contant_k, person_weight_kg):
        self.bungee_length_m = bungee_length_m
        self.spring_constant_k = spring_contant_k
        self.person_weight_kg = person_weight_kg
        self.gravity = - 9.81 #m/s^2
        # Initial condition, before the bungee tightens
        self.t0 = - np.sqrt(-1*bungee_length_m/self.gravity)
        self.y0 = self.t0**2*self.gravity
        self.v0 = self.t0*self.gravity
    
    def velocity_func(t, ??):
        """ The dynamic equation is:
        dv/dt = gravity + 
        F = ma, a =F/m