# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:39:36 2020

@author: Aryaman
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

x_min = -2.5
x_max = 1.
y_min = -1.25
y_max = 1.25
n = 1000
x = np.linspace(x_min, x_max, int(abs(x_max - x_min)*n))
y = np.linspace(y_min, y_max, int(abs(y_max - y_min)*n))
threshold = 100

def imgmat(x,y):
    values = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
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
            values[i][j] = count**0.3
    return values
        
def plot():       
    plt.figure(figsize = (10*(1366/768), 10), dpi = 100)
    plt.imshow(np.transpose(imgmat(x,y)), extent = [x_min, x_max, y_min, y_max], cmap = "twilight_shifted", interpolation = "gaussian")
    
plot()    
print("Run time is : %s" %(time.time() - start_time))             
                
                

