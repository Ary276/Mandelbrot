# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:19:18 2020

@author: Aryaman
"""


import numpy as np
import matplotlib.pyplot as plt
import time
from numba import njit, prange
import matplotlib.animation as animation

start_time = time.time()

n = 1000

x_i = -2
x_f = -1.2489481321697
y_i = -1.25
y_f = -0.04938967921937
w_i = 2.5
w_f = 0.000000000000025
h_i = 2.5
h_f =  0.000000000000025


f = 1000

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
            values[i][j] = count**0.1
    return values
        
fig = plt.figure(figsize = (10, 10), dpi = 100)
ax = plt.axes()


def animate(i):
    ax.clear()
    ax.set_axis_off()
    s = (i/(f-1))**(1.04**(-i))
    x_min = x_i  + (x_f-x_i)*s
    y_min = y_i + (y_f-y_i)*s
    width = w_i + (w_f-w_i)*s
    height = h_i + (h_f-h_i)*s
    zoom = np.log10(w_i/width)
    threshold = round(100 + 700*s)
    x = np.linspace(x_min, x_min + width, n)
    y = np.linspace(y_min, y_min + height, n)
    img = plt.imshow(np.transpose(imgmat(x,y, threshold)), extent = [x_min, x_min + width, y_min, y_min  + height], cmap = "magma", interpolation = "bicubic", aspect = "equal")
    plt.text(x_min, y_min, "$10^{{{:.2f}}}$".format(zoom), color="black", fontsize = 30, bbox=dict(facecolor='white', alpha=0.5, pad=10))
    return [img]


anim = animation.FuncAnimation(fig, animate, frames=f, interval= 40, blit=True) 
anim.save('mandelbrotzoom6.mp4',writer= "ffmpeg", savefig_kwargs={'facecolor': 'black'})
    
print("Run time is : %s" %(time.time() - start_time))              
                
                

