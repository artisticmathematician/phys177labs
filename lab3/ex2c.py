"""
Created on Sun Apr 26 12:34:25 2015
This is the second part of the Kirchhoff current law problem conssisting of 
solving thhe 4x4 matrix via gaussian elimination.
@author: Chris
"""

import scipy
import scipy.linalg 
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

#Diagonal, Lower triangular, and upper triangular matrices respectively. 
D, L, U = np.around(scipy.linalg.lu(V), 2)

#The direct solution
DirSol = np.linalg.solve(V, vect)

#The LU solution
Y = np.linalg.solve(L, vect)
LUsol = np.around(np.linalg.solve(U, Y), 1)

print "\nMy matricies are as follows:\n"
print "The originonal matrix with the solution matrix:\n\n", V, '\n\n', vect
print "\nThe upper and lower triangular matricies from using scipy.linalg.lu(V)"
print "\nLower Triangular matrix:\n", L
print "\nUpper Triangular matric:\n", U
print "\nThe result from solving the matrix with LU elimination is:", LUsol
print "\nThe result from  solving the matirx with np.linalg.solve is:", DirSol
