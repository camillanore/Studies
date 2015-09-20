# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:09:39 2015

@author: NBCNO1
"""
"""
The program from Exercise 4.10 reads input from the command line. Extend
that program with exception handling such that missing commandline
arguments are detected. In the except IndexError block, use the
raw_input function to ask the user for missing input data.
Husk: det vi skal vise er at det er riktig antall argumenter inn i funksjonen. 
(typ om det er for få)
"""

try:
    t = float(sys.argv[1])
    v_0 = float(sys.argv[2])

except:
    print "t and v_o need to be numbers."
    t = float(raw_input("t = "))
    v_o = float(raw_input("v_0 = "))

def y(g, t, v_0):
     y = v_0*t - 0.5*g*t**2
     except ValueError:
        print "\nNot a number\n"
        sys.exit(1)
     return y

print "The solution for y is ", y_t(g, t, v_0)