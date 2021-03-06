# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/192-EpTp1dV-u2xEVvsGgjcDCmsEoovqS
"""

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sympy import *

#To label the points # 
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
plt.annotate("A[0,6]",(0,6))
plt.annotate("B[0,0]",(0,0))
plt.annotate("C[8,0]",(8,0))
plt.plot(AB_X,AB_Y)
plt.plot(AC_X,AC_Y)
plt.plot(BC_X,BC_Y)
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
 
D = [72/25,96/25]
BD_X = [0,72/25]
BD_Y = [0,96/25]
plt.scatter(D[0],D[1],color='black')
plt.annotate("D",(72/25,96/25))
plt.plot(BD_X,BD_Y)


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
x_circ1= circ_gen(Ce,r)
plt.scatter(Ce[0],Ce[1],color='black')
plt.annotate("Centre[4,0]",[4,0])
plt.plot(x_circ1[0,:],x_circ1[1,:],label='Circumcircle')

plt.legend()
plt.grid()
plt.show()