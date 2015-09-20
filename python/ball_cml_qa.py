# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:09:39 2015

@author: Camilla Nore
"""
"""
Exercise 4.11: 
The program from Exercise 4.10 reads input from the command line. Extend
that program with exception handling such that missing commandline
arguments are detected. In the except IndexError block, use the
raw_input function to ask the user for missing input data.
Husk: det vi skal vise er at det er riktig antall argumenter inn i funksjonen. 
(typ om det er for få)
"""
import sys

try:
    t = float(sys.argv[1])
    v_0 = float(sys.argv[2])
    print "You hav given", len(sys.argv), "arguments."
except IndexError as e:
    print "Not enough argumenets given, please give manually:"
    t = raw_input("t = ")
    v_0 = raw_input("v_0 = ")

# At this point we are sure that we have two values.
# Want to convert them to floats.
                
try:
    t = float(t)
    v_0 = float(v_0)
except ValueError as e:
    print "\nNot a number\n", e
    sys.exit(1)


def y_t(g, t, v_0):
    y = v_0*t - 0.5*g*t**2
    return y

g = 9.81
print "The solution for y is ", y_t(g, t, v_0)

"""
Output without arguments:

Not enough argumenets given, please give manually:
t = v_0 = The solution for y is  -32.145

Output with too few arguments:

C:\Users\NBCNO1\Documents\Studies\python>python ball_cml_qa.py 3
Not enough argumenets given, please give manually:
t = 3
v_0 = 4
The solution for y is  -32.145

Output when argument is not a number:

C:\Users\NBCNO1\Documents\Studies\python>python ball_cml_qa.py 3
Not enough argumenets given, please give manually:
t = hei
v_0 = 3

Not a number
could not convert string to float: hei
"""