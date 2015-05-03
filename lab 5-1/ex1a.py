"""
Created on Sun May 03 09:47:55 2015
This program is meant to explore polynomials 
@author: Chris
"""

import math
import matplotlib.pyplot as plt

# c == coefficent 
c1 = 924.0
c2 = -2772.0
c3 = 3150.0
c4 = -1680.0
c5 = 420.0
c6 = -42.0
c7 = 1.0

def poly(x):
    y = (c1*math.pow(x, 6) + c2*math.pow(x, 5) + c3*math.pow(x, 4) + 
        c4*math.pow(x, 3) + c5*math.pow(x, 2) + c6*x + c7)
    return y

n = 100
i = 0
x = 0.0
y = 0.0
xi = 0.0
xf = 1.0
dx = (xf - xi)/100.0
xdata = []
ydata = []

while (i < n):
    y = poly(x)
    xdata.append(x)
    ydata.append(y)
    x = x + dx
    i = i + 1

plt.scatter(xdata, ydata)
plt.title("Polynomial Graph X vs. Y from 0 to 1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.savefig('ex1aGraph.png')

print "The roots, in the range from 0.0 to 1.0, from looking at the graph, appear to be:"
print "[0.97, 0.84, 0.62, 0.39, 0.17, 0.01]"
