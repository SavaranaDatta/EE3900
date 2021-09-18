# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pqohCrBh0rhjyIkVszvPRgsBKXQgcjTT
"""

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sympy import *

X = [0,0,8]
Y = [6,0,0]

A = [0,6]
B = [0,0]
C = [8,0]

AB_X = [0,0]
AB_Y = [6,0]
AC_X = [0,8]
AC_Y = [6,0]
BC_X = [0,8]
BC_Y = [0,0]

figure(figsize=(5,6))
plt.scatter(X,Y,color='black')
plt.annotate("A",(0,6))
plt.annotate("B",(0,0))
plt.annotate("C",(8,0))
plt.plot(AB_X,AB_Y)
plt.plot(AC_X,AC_Y)
plt.plot(BC_X,BC_Y)
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
 
M = [36/13,24/13]
plt.scatter(M[0],M[1],color='black')
plt.annotate("M",(36/13,24/13))
P = [72/13,48/13]
plt.scatter(P[0],P[1],color='black')
plt.annotate("P",(72/13,48/13))

def circ_gen(C,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

Ce = [4,0]
r = 4

ACe_X = [0,4]
ACe_Y = [6,0]
AP_X = [0,72/13]
AP_Y = [6,48/13]
BP_X = [0,72/13]
BP_Y = [0,48/13]

x_circ1= circ_gen(Ce,r)
plt.scatter(Ce[0],Ce[1],color='black')
plt.annotate("C1",[4,0])
plt.plot(x_circ1[0,:],x_circ1[1,:],label='Circumcircle')
plt.plot(ACe_X,ACe_Y)
plt.plot(AP_X,AP_Y)
plt.plot(BP_X,BP_Y)
plt.legend()
plt.grid()
plt.show()