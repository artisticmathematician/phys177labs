"""
Created on Sat Apr 11 13:57:42 2015
This program is desined to explore integration via simpsoms and 
trapazoidal rule.
@author: Chris Cosio
"""
### To the grader/professor

### I still included ex3 even though it's not due yet. If you have the free 
### time to provide any feedback, that would be great. I am having issues with 
### my functions I think. My functions do not return a value close to the known 
### value.

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
    y = math.pow(x,2) - 2*x + 1
    return (y)

dataX = []
dataY = []
data = []
i = 0
n = 5
x1 = input("Enter intial domain value:")
x2 = input("ENter final domain value:")
dx = (x2*1.0 - x1*1.0)/20.0
while (i <= n):
    y = funcX(x1)
    dataX.append(x1)
    dataY.append(y)
    data.append([x1,y])
    x1 = x1 + dx
    i = i + 1

trap_resultMe = trap_rule(data)
simp_resultMe = simp_rule(data)
trap_resultPy = numpy.trapz(data)
simp_resultPy = simps(data)
known_result = 4.4


print "My trapeziod rule resulted in: ", trap_resultMe
print "The numpy trapezoid rule resulted in: ", trap_resultPy
print "My simpson's rule resulted in: ", simp_resultMe
print "The numpy simpson's rule resulted in: ", simp_resultPy
print "The value from integration by hand is: ", known_result
 