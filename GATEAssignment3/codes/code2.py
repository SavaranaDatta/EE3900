# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZAIn6_e1dtY3NzNYPc1UFq1hDXaDrtsE
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import pi
from scipy.fft import fft,fftshift

samp_rate = 700
time = np.linspace(-1,1,2*samp_rate)
output = (6*(10**4)*((np.sinc(700*time))**2))+((10**6)*((np.sinc(500*time))**(3)))
# plot of the given signal
plt.stem(time,output)
plt.xlim(-0.015,0.015)
plt.grid()
plt.show()