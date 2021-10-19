# -*- coding: utf-8 -*-
"""GATE Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OZCueGLKSFr1JwnZ9d_5Sy6k6aOBSGcW
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import abs
import math

def sinc(x):
    if (x==0):
        return 1    
    else:
       return (math.sin(x))/(x)


X = np.linspace(-15,15,1000000)
Y = [(2*sinc(x)) for x in X]
plt.xlabel('w')
plt.ylabel('$x(f)=2sinc(2f)$')
plt.scatter([0],[0],c='red')
plt.scatter([math.pi],[0],c='blue')
plt.scatter([2*math.pi],[0],c='blue')
plt.scatter([0.5*math.pi],[0],c='red')
plt.scatter([1.5*math.pi],[0],c='red')
plt.scatter([2.5*math.pi],[0],c='red')
plt.plot(X,Y)
plt.grid()
plt.show()