"""
Created on Sun Apr 26 12:34:25 2015
This is the first part of the Kirchhoff current law problem conssisting of a 
list of equations and the matrix that will be used in part b and c.
@author: Chris
"""

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
V = matrix([[4, -1, -1, -1, 5], [-1, 3, 0, -1, 5], [-1, 0, 3, -1, 5], 
      [-1, -1, -1, 4, 5]])

print V
