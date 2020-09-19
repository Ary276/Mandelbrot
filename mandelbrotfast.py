# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:57:04 2020

@author: Aryaman
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from numba import njit, prange

start_time = time.time()

x_min = -1.2489481321697
x_max = x_min + 0.0000000000000275
y_min = -0.04938967921937
y_max = y_min +  0.000000000000025
n = 100
x = np.linspace(x_min, x_max, n)
y = np.linspace(y_min, y_max, n)
threshold = 1000

@njit(parallel = True, fastmath= True)
def imgmat(x,y):
    values = np.zeros((len(x), len(y)))
    for i in prange(len(x)):
        for j in prange(len(y)):
            z = complex(0,0)
            c = complex(x[i],y[j])
            count = 0
            for k in range(threshold):
                if (abs(z) > 2):
                    break
                else:
                    z = z**2 + c
                    count += 1
                    pass
            values[i][j] = count**0.1
    return values
 
      
plt.figure(figsize = (10, 10), dpi = 100)
plt.axis("off")
plt.imshow(np.transpose(imgmat(x,y)), extent = [x_min, x_max, y_min, y_max], cmap = "magma", interpolation = "bicubic")
plt.text(x_min, y_min, "$10^{-5}$", color="black", fontsize = 30, bbox=dict(facecolor='white', alpha=0.5, pad=10))
print("Run time is : %s" %(time.time() - start_time))              
                
                

