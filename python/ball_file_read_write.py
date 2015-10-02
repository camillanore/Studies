# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:35:47 2015

@author: Camilla Nore
"""

"""
v0: 3.00
t:
0.15592 0.28075 0.36807889 0.35 0.57681501876
0.21342619 0.0519085 0.042 0.27 0.50620017 0.528
0.2094294 0.1117 0.53012 0.3729850 0.39325246
0.21385894 0.3464815 0.57982969 0.10262264
0.29584013 0.17383923
More precisely, the first two lines are always present, while the next lines
contain an arbitrary number of t values on each line, separated by one
or more spaces.
a) Write a function that reads the input file and returns v0 and a list
with the t values. 

b) Write a function that creates a file with two nicely formatted columns
containing the t values to the left and the corresponding y values to the
right. Let the t values appear in increasing order (note that the input
file does not necessarily have the t values sorted).
c) Make a test function that generates an input file, calls the function
for reading the file, and checks that the returned data objects are correct.
Filename: ball_file_read_write.py.
"""
# Exercise 4.14 Evaluate a formula for data in a file

#def extract_data(data.txt):
infile = open(data.txt, 'r') # tells that we eant to open the file for reading
infile.readline() #skip the first line
infile.readline() #skip the second line
lines =infile.readlines()
v0 = []
t = []
for line in lines[3:]:
words = line.split()
t_ = float(words[-1])
F.append(t_)
infile.close()
print v0, t

def extract_data(filename):
infile = open(filename, ’r’)
infile.readline() # skip the first line
data = [line.split() for line in infile]
annual_avg = data[-1][1]
data = [(m, float(r)) for m, r in data[:-1]]
infile.close()
return data, annual_avg

# i b skal sortere, bruk: sortet(t)
    