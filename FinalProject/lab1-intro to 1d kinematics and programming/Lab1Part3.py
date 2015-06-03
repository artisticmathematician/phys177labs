# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:48:20 2015
A simple program that solves for final position of an object
@author: Chris
"""
x0 = input("Please enter the initial position of the object meters: ")
v0 = input("Please enter the initial velocity of the object in m/s: ")
a = input("Please enter the acceleration of the object m/s^2: ")
t = input("Please enter the travel time of the object in seconds: ")

xf = x0 + v0*t + 0.5*a*t*t
print "The final position is ", xf, " meters."
