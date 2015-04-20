"""
Created on Sat Apr 11 13:57:42 2015
This program is desined to explore integration via simpsoms and 
trapazoidal rule.
@author: Chris Cosio
"""

import math
import numpy
from scipy.integrate import simps
    
def trap_rule (list):
    i = len(list)
    j = 0 
    area = 0
    dx = (list[j+1][0] - list[j][0])
    k = dx/2
    while (j < i - 1):
        if((j != 0) and (j != (i - 2))):
            c = 2
        if((j == 0) or (j == (i - 2))):
            c = 1
        area = area + c*k*list[j][1]
        j = j + 1
    return (area)

def simp_rule (list):
    i = len(list)
    delx = list[1][0] - list[0][0]
    j = 0
    area = 0
    while (j < i - 1):
        if ((j%2 != 0) and (j != 0) and j != (i - 2)):
            c = 4
        if ((j%2 == 0) and (j != 0) and j != (i - 2)):
            c = 2
        if (j == 0) or j == (i - 2):
            c = 1
        area = area + c*(delx/3)*list[j][1]
        j = j + 1
    return (area)

def funcX (x):
    y = math.pow(x,4) - 2*x + 1
    return (y)

dataX = []
dataY = []
data = []
dataHalfX = []
dataHalfY = []
i = 0
j = 0
n = input("\nEnter the number of slices (enter 20 for lab 2 exercise 3): ")
n = n*1.0
nHalf = n/2.0
x1 = input("\nEnter intial domain value (enter 0 for lab 2 exercise 3): ")
x2 = input("\nEnter final domain value (enter 2 for lab 2 exercise 3): ")
x1Half = x1
dx = (x2*1.0 - x1*1.0)/n
dxHalf = (x2*1.0 - x1*1.0)/nHalf

while (i <= n):
    y = funcX(x1)
    dataX.append(x1)
    dataY.append(y)
    data.append([x1,y])
    x1 = x1 + dx
    i = i + 1
    
while  (j <= nHalf):
    y = funcX(x1Half)
    dataHalfX.append(x1Half)
    dataHalfY.append(y)
    x1Half = x1Half + dxHalf
    j = j + 1
    

trap_resultMe = trap_rule(data)
simp_resultMe = simp_rule(data)
trap_resultPy = numpy.trapz(dataY, dataX)
simp_resultPy = simps(dataY, dataX)
known_result = 4.4
trapError = 1.0/3.0*(numpy.trapz(dataY, dataX) - numpy.trapz(dataHalfY, dataHalfX))
simpError = 1.0/15.0*(simps(dataY, dataX) - simps(dataHalfY, dataHalfX))

print "\n-----------------------------------"
print "\nMy trapeziod rule resulted in:", trap_resultMe
print "\nThe numpy trapezoid rule resulted in:", trap_resultPy
print "\nMy simpson's rule resulted in:", simp_resultMe
print "\nThe numpy simpson's rule resulted in:", simp_resultPy
print "\nThe value from integration by hand is:", known_result
print "\nThe practical error estimate for the trapezoid rule is:", trapError
print "\nThe practical error estimate for the simpsom rule is:", simpError
 