# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:00:19 2015

@author: NBCNO1
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
%matplotlib inline

def animate_series(fk,M,N,xmin,xmax,ymin,ymax,n,exact):
    import glob, os
    x = np.linspace(xmin,xmax,n)
    s = np.zeros_like(x)
    s_ref = exact(x)

    old_files = glob.glob('tmp_*.png')
    for file in old_files:
        os.remove(file)

    plt.ion() #turn matplotlib interactive mode on
    plt.plot(x,s_ref)
    lines = plt.plot(x,s)
    plt.axis([xmin,xmax,ymin,ymax])

    framenumber = 0
    for k in range(M,N+1):
        s += fk(x,k)
        lines[0].set_ydata(s)
        plt.draw()
        plt.savefig('tmp_%04d.png' %framenumber)
        framenumber += 1
        time.sleep(.5) #wait 0.5 seconds per frame

def taylor_sin(x,k):
    return (-1)**k*x**(2*k+1)/math.factorial(2*k+1)

animate_series(taylor_sin,0,40,0,13*math.pi,-2,2,100,np.sin)

def taylor_exp_mx(x,k):
    return (-x)**k/math.factorial(k)

def exp_mx(x):
    return exp(-x)

#animate_series(taylor_exp_mx,0,30,0,15,-0.5,1.4,100,exp_mx)