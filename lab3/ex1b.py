"""
Created on Sat Apr 25 13:55:27 2015
This program was created to explore the graph of electric fields generated by 
two point charges.
@author: Chris Cosio
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show, xlabel, ylabel
from mpl_toolkits.mplot3d import Axes3D

e = 8.854187817

def E(x,y):
    if ((x - 0.1 == 0) or (x + 0.1 == 0)):
        E = 0
    if ((x - 0.1 != 0) & (x + 0.1 != 0)):
        E1x = -(x - 1)/(4*math.pi*e*math.pow((math.pow((x - 1),2) + y*y),3/2))
        E1y = -(y)/(4*math.pi*e*math.pow((math.pow((x - 1),2) + y*y),3/2))
        E2x = -(x + 1)/(4*math.pi*e*math.pow((math.pow((x + 1),2) + y*y),3/2))
        E2y = -(y)/(4*math.pi*e*math.pow((math.pow((x + 1),2) + y*y),3/2))
        E = E1x + E1y + E2x + E2y
    
    if(E > 0.08):
        E = 0.08
    if(E < -0.08):
        E = -0.08

    return (E)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-0.5, 0.5, 0.01)
X, Y = np.meshgrid(x, y)
zs = np.array([E(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_wireframe(X, Y, Z, rstride = 2, cstride = 2)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('E (V/m)')