"""
Created on Sat Apr 25 13:55:27 2015
This program was created to explore the graph of electrical potential generated
by two point charges.
@author: Chris Cosio
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show, xlabel, ylabel
from mpl_toolkits.mplot3d import Axes3D

e = 8.854187817

def phi(x,y):
    if ((x - 0.1 == 0) or (x + 0.1 == 0)):
        phi = 0
    if ((x - 0.1 != 0) & (x + 0.1 != 0)):
        x1 = x + 0.1
        r = (math.sqrt(x1*x1 + y*y))
        phi1 = -1/(4*math.pi*e*r)
    
        x2 = x - 0.1
        r = (math.sqrt(x2*x2 + y*y))
        phi2 = 1/(4*math.pi*e*r)
        phi = phi1 + phi2
    
    if(phi > 0.08):
        phi = 0.08
    if(phi < -0.08):
        phi = -0.08

    return (phi)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-0.5, 0.5, 0.01)
X, Y = np.meshgrid(x, y)
zs = np.array([phi(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_wireframe(X, Y, Z, rstride = 2, cstride = 2)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Phi (V)')