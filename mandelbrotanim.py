# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:39:30 2020

@author: Aryaman
"""


import numpy as np
import matplotlib.pyplot as plt
import time
from numba import njit, prange
import matplotlib.animation as animation

start_time = time.time()

x_min = -2
x_max = 0.75
y_min = -1.25
y_max = 1.25
n = 1000
x = np.linspace(x_min, x_max, int(abs(x_max - x_min)*n))
y = np.linspace(y_min, y_max, int(abs(y_max - y_min)*n))
#threshold = 1000

@njit(parallel = True, fastmath= True)
def imgmat(x,y, threshold):
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
            values[i][j] = count**0.3
    return values
        
fig = plt.figure(figsize = (10, 10), dpi = n/10)
ax = plt.axes()

def animate(i):
    ax.clear()  # clear axes object
    #ax.set_xticks([], [])  # clear x-axis ticks
    #ax.set_yticks([], [])  # clear y-axis ticks
    
    threshold = round(1.15**(i + 1))  # calculate the current threshold
    img = plt.imshow(np.transpose(imgmat(x,y, threshold)), extent = [x_min, x_max, y_min, y_max], cmap = "twilight_shifted", interpolation = "bicubic")
    return [img]

anim = animation.FuncAnimation(fig, animate, frames= 90, interval=40, blit=True) 
anim.save('mandelbrotform.mp4',writer= "ffmpeg")   
print("Run time is : %s" %(time.time() - start_time))              
                
                

