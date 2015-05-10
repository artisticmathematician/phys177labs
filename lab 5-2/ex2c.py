"""
Created on Sat May 09 20:04:37 2015
This program is designed to examine three functions and their FFTs.
@author: Chris Cosio
"""

import scipy
import numpy as np
import math
import matplotlib.pyplot as plt

#I wrote the functions and arrays for all three parts of problem 2
#Each part, 2a, 2b, and 2c, will be modified to output the correct
#graph and print information for the relative part. I also custome wrote
#the first two functions below to populate an array with data that simulates
#either a square or saw wave respectively. 
def square(x):
    y = -50
    if ((x >= 0) & (x < 1)):
        y = 1
    if ((x >= 1) & (x < 2)):
        y = -1
    return y
    
def sawtooth(x):
    xdecimal = math.sqrt(math.pow(x%1, 2))
    y = 2*xdecimal - 1.0
    return y
    
def sinemodu(x):
    y = math.sin(math.pi*x/1000.0)*math.sin(20*math.pi*x/1000.0)
    return y

xlist = []
sqdatay = []
sawdatay = []
sinedatay = []
i = 0
n = 1000
x = 0
x1 = 0.0
x2 = 2.0
dx = (x2 - x1)/1000.0

while (i < n):
    xlist.append(x)
    sqdatay.append(square(x))
    sawdatay.append(sawtooth(x))
    sinedatay.append(sinemodu(x))
    i = i + 1
    x = x + dx

sqA = []
sawA = []
sineA = []
fftsq = scipy.fft(sqdatay)
fftsaw = scipy.fft(sawdatay)
fftsine = scipy.fft(sinedatay)
j = 0

while (j < len(fftsq)):
    sqA.append(math.sqrt(np.conjugate(fftsq[j])*fftsq[j]))
    sawA.append(math.sqrt(np.conjugate(fftsaw[j])*fftsaw[j]))
    sineA.append(math.sqrt(np.conjugate(fftsine[j])*fftsine[j]))
    j = j + 1

print "The coefficence values are 0 and 2"
plt.scatter(xlist, sineA)
plt.ylim(-0.1, 0.1)
plt.xlim(-3, 3)
plt.title("Amplitude Values")
plt.xlabel("Amplitude")
plt.ylabel("Counts")
plt.show()

    












