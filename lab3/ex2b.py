"""
Created on Sun Apr 26 12:34:25 2015
This is the second part of the Kirchhoff current law problem conssisting of 
solving thhe 4x4 matrix via gaussian elimination.
@author: Chris
"""

import numpy as np
from numpy import matrix

v1 = 1
v2 = 1
v3 = 1
v4 = 1
v5 = 5

#Given eq.
E1 = 4*v1 - v2 - v3 - v4 - 5

#Other Eq.
E2 = -v1 + 3*v2 - (0)*v3 -v4 - 5
E3 = -v1 + (0)*v2 + 3*v3 -v4 - 5
E4 = -v1 + v2 - v3 -4*v4 - 5

#coefficient matrix
V = matrix([[4.0, -1.0, -1.0, -1.0], [-1.0, 3.0, 0.0, -1.0], 
            [-1.0, 0.0, 3.0, -1.0], [-1.0, -1.0, -1.0, 4.0]])
#solution Matrix
vect = [5.0, 5.0, 5.0, 5.0]

#program that solves the matrix via gaussian elimination had some trouble with
#my loops so I just did this the long way.
max = np.max(V[0])
V[0] = V[0]/max
vect[0] = vect[0]/max
V[1] = V[1] + V[0]
vect[1] = vect[1] + vect[0]
V[2] = V[2] + V[0]
vect[2] = vect[2] + vect[0]
V[3] = V[3] + V[0]
vect[3] = vect[3] + vect[0]

print "\n\nstep 1:\n", V, "\n", np.around(vect, 2)

max = np.max(V[1])
V[1] = np.around(V[1]/max, 2)
vect[1] = vect[1]/max
V[0] = np.around(V[0] + 0.25*V[1], 2)
vect[0] = vect[0] + 0.25*vect[1]
V[2] = np.around(V[2] + 0.25*V[1], 2)
vect[2] = vect[2] + 0.25*vect[1]
V[3] = np.around(V[3] + 1.25*V[1], 2)
vect[3] = vect[3] +1.25* vect[1]

print "\n\nstep 2:\n", V, "\n", np.around(vect, 2)

max = np.max(V[2])
V[2] = np.around(V[2]/max, 2)
vect[2] = vect[2]/max
V[0] = np.around(V[0] + 0.272*V[2], 2), 
vect[0] = vect[0] + 0.272*vect[2]
V[1] = np.around(V[1] + 0.0909*V[2], 2)
vect[1] = vect[1] + 0.0909*vect[2]
V[3] = np.around(V[3] + 1.363*V[2], 2)
vect[3] = vect[3] +1.25* vect[2]

print "\n\nstep 3:\n", V, "\n", np.around(vect, 2)

max = np.max(V[3])
V[3] = V[3]/max
vect[3] = vect[3]/max
V[0] = np.around(V[0] + 0.5*V[3], 2), 
vect[0] = vect[0] + 0.5*vect[3]
V[1] = np.around(V[1] + 0.5*V[3], 2)
vect[1] = vect[1] + 0.5*vect[3]
V[2] = np.around(V[2] + 0.5*V[3], 2)
vect[2] = vect[2] + 0.5*vect[3]

print "\n\nstep 4:\n", V, "\n", np.around(vect)
print "\n\nThe solution vector is:"
print matrix(np.around(vect))
