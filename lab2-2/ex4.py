"""
Created on Sat Apr 11 13:57:42 2015
This program is desined to explore integration via simpsoms and 
trapazoidal rule.
@author: Chris Cosio
"""

import math
import numpy

def funcX (x):
    y = math.pow(math.sin(math.sqrt(100*x)),2)
    return (y)
    
dataX = []
dataY = []
dataHalfX = []
dataHalfY = []
flag = 0
error = 1.0
i = 0
j = 0
k = 0
n = input("\nEnter the number of slices (enter 1 for lab 2 exercise 4): ")

while ((n <= 0) or (((n*1.0)%1.0) != 0)):
    n = input("\nInvalid input, N must be a positive integer, please retry: ")
    
x1 = input("\nEnter initial domain value (enter 0 for lab 2 exercise 4): ")
const1 = x1
x2 = input("\nEnter final domain value (enter 1 for lab 2 exercise 4): ")
const2 = x2

while (flag != 2):
    dataX = []
    dataY = []
    dataHalfX = []
    dataHalfY = []
    x1 = const1
    x2 = const2
    i = 0
    j = 0
    k = k + 1
    n = n*1.0
    nHalf = n/2.0
    x1Half = x1
    dx = (x2*1.0 - x1*1.0)/n
    dxHalf = (x2*1.0 - x1*1.0)/nHalf
    
    while (i <= n):
        y = funcX(x1)
        dataX.append(x1)
        dataY.append(y)
        x1 = x1 + dx
        i = i + 1
        
    while  (j <= nHalf):
        y = funcX(x1Half)
        dataHalfX.append(x1Half)
        dataHalfY.append(y)
        x1Half = x1Half + dxHalf
        j = j + 1
        
    trap_resultPy = numpy.trapz(dataY, dataX)
    known_result = 0.45
    iDiff = (numpy.trapz(dataY, dataX) - numpy.trapz(dataHalfY, dataHalfX))
    trapError = math.sqrt(math.pow((1.0/3.0*iDiff),2))

    print "\n--------------- Iteration #", k, "---------------"
    print "\nThe number of slices used was:", int(n)
    print "\nThe trapezoid rule resulted in:", trap_resultPy
    print "\nThe known integration value is:", known_result
    print "\nThe error estimate for the trapezoid rule is:", trapError
    print "\nWould you like to double the slices or end the program?"
    print "\nEnter 0 to double the slices"
    print "Enter 1 to automate the process until six digits of accuracy is achieved"
    print "Enter 2 to close the program"
    flag = input("Input: ")
    
    while ((flag != 1) & (flag != 0) & (flag != 2)):
        print "\nInvalid input\n"
        print "Enter 0 to double the slices"
        print "Enter 1 to automate the process until six digits of accuracy is achieved"
        print "Enter 2 to close the program"
        flag = input("Input: ")
        
    while ((flag == 1) & (error >= 0.00001)):
        dataX = []
        dataY = []
        dataHalfX = []
        dataHalfY = []
        x1 = const1
        x2 = const2
        i = 0
        j = 0
        
        n = n*1.0
        nHalf = n/2.0
        x1Half = x1
        dx = (x2*1.0 - x1*1.0)/n
        dxHalf = (x2*1.0 - x1*1.0)/nHalf
        
        while (i <= n):
            y = funcX(x1)
            dataX.append(x1)
            dataY.append(y)
            x1 = x1 + dx
            i = i + 1
            
        while  (j <= nHalf):
            y = funcX(x1Half)
            dataHalfX.append(x1Half)
            dataHalfY.append(y)
            x1Half = x1Half + dxHalf
            j = j + 1
            
        trap_resultPy = numpy.trapz(dataY, dataX)
        known_result = 0.45
        iDiff = (numpy.trapz(dataY, dataX) - numpy.trapz(dataHalfY, dataHalfX))
        trapError = math.sqrt(math.pow((1.0/3.0*iDiff),2))
        error = trapError
        n = n*2.0
        
        if (error <= 0.00001):
            flag = 2
            print "\n--------------- Iteration #", k, "---------------"
            print "\nThe number of slices used was:", int(n)
            print "\nThe trapezoid rule resulted in:", trap_resultPy
            print "\nThe value from integration by hand is:", known_result
            print "\nThe error estimate for the trapezoid rule is:", trapError
            
        k = k + 1
        
    
    n = n*2.0
        

 