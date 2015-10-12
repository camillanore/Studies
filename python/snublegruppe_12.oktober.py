# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:49:31 2015

@author: NBCNO1
"""

import matplotlib.pyplot as plt
from time import sleep
import numpy as np

plt.ion() #interactive on

x = np.linspace(0, 1, 100)

for i in range(10): 
    plt.clf()
    plt.plot(x, x*i)
    axis([0, 1, 0, 10])
    plt.draw()
    #savefig('anim_%04d.png' % i)
    sleep(0.2)

plt.ioff()
plt.show()