# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 15:22:23 2015

@author: Camilla Nore
"""
# Exercise 2.10 s=sum(1/k) for k=1 to M=100
#Explain why the following program does not work
#s = 0; k = 1; M = 100
#while k < M:
#s += 1/k
#print s

k = 1.0
s = 0
M = 100

# You can write this loop in two ways, using while:
while k < M:
    s += 1.0/k
    k += 1
print 'While loop, Sum of 1/n: ', s

# Or using for:

s2 = 0.0
for k in range(1,M):
    s2 += 1.0/k
print 'For loop, Sum of 1/n: ', s2


terminal

While loop, Sum of 1/n:  5.17737751764
For loop, Sum of 1/n:  5.17737751764
