"""
Created on Sat May 23 18:57:09 2015
This is the working fan cart simulation for lab 2
@author: Chris
"""
from __future__ import division
from visual import*

mcart = 0.80 #mass in kilograms
vcart = vector(0.5, 0, 0.15) #intial velocity of cart
vlist = [] #empty velocity array
vlist.append(vcart) #adds vcart to the end of vlist
t = 0 #initial time
i = 0
deltat = 0.01 #change in time in seconds
fEx = vector(0.0526, 0, 0.016)#External force acting upon the cart

while t <= 15.2:
    vcart = vcart - fEx*deltat/mcart #Change in velocity
    vlist.append(vcart)#adds vcart to the end of vlist
    t = t + deltat
    i = i + 1
    
accAVG = (vlist[i - 1] - vlist[0])/(15.19) #statement for avg acceleration
forceAVG = accAVG*mcart #statement for avergae force
print "The force vector I calculated was: ", forceAVG
print "The external force exerted on the fancart was: ", fEx