"""
Created on Sat May 23 18:57:09 2015
This is the working fan cart simulation for lab 2
@author: Chris
"""
from __future__ import division
from visual import*

mcart = 0.80 #mass in kilograms
pcart = mcart*vector(0.5,0,0.15) #momentum of cart
t = 0 #initial time
deltat = 0.01 #change in time in seconds
fEx = vector(0.0526,0,0.016)#External force acting upon the cart
print "cart momentum = ", pcart
track = (box(pos = vector(0, -0.025, 0), 
             size = (2.0, 0.05, 1.75), color = color.white))
cart = (box(pos = vector(0.95, 0.027, 0), 
           size = (0.1, 0.04, 0.06), color = color.green))

while t <= 15.2:
    rate(100)
    pcart = pcart - fEx*deltat #Change in momentum
    cart.pos = cart.pos - (pcart/mcart)*deltat #Change in cart position.
    t = t + deltat
print('end of program')