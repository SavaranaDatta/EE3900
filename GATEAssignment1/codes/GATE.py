# -*- coding: utf-8 -*-
"""GATE0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UbHz1cbVuShvLVqw6Bknuhs2qXxfO9Im
"""

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from math import *

time = np.arange(0,100,0.00001)

Amplitude = 1 + (2*np.cos(pi*time)) + (3*np.sin(2*pi*time/3))+ (4*np.cos((pi*time/2)+(pi/4)))
tp_1 = 2
tp_2 = 3
tp_3 = 4

plt.plot(time,Amplitude)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

def lcm1(a,b):
  return int(a*b/gcd(a,b))
  

def lcm(a,b,c):
  return lcm1(lcm1(a,b),c)
    
ftp = lcm(tp_1,tp_2,tp_3)

print("Fundamental Time Period:",ftp,"sec")

plt.axvline(0,0,1,color = 'r',label='Fundamental Time Period Interval')
plt.axvline(ftp,0,1,color='r')
plt.legend()
plt.show()