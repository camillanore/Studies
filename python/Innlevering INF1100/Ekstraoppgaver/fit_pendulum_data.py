# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:56:07 2015

@author: Camilla Nore

Exercise 5.18: Fit a polynomial to experimental data

"""
import numpy as np
import matplotlib.pyplot as plt


def main():
    infile = open('pendulum.dat', 'r')
    infile.readline()
    L = []
    T = []
    for line in infile:
        x, y = [float(w) for w in line.split()]
        L.append(x)
        T.append(y)
    plt.plot(L, T, 'o')
    plt.xlabel('L')
    plt.ylabel('T')
    
    for degree in range(1,4):
        coeff = np.polyfit(L, T, degree)
        p = np.poly1d(coeff)
        T_fitted = p(L)
        plt.plot(L, T_fitted, label = 'poly%d' %degree)
    plt.legend(loc='best')
    plt.show()
if __name__ == '__main__':
    main()

"""Output:

See graph. The polynomial of degree 3 fits the measured data best.

"""