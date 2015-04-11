"""
Lab Assignment 1-ex3A
Created on Fri Apr 10 16:03:31 2015
This program is a simulator for the amount of time it takes for a ball to
reach the bottom of a tower when thrown from the top of the tower.
@author: Chris Cosio
"""

import math

flag = 0
h = 800.0
g = -9.81
while (flag == 0):
    vel_0 = raw_input("Please enter an integer for intial velocity: ")
    flag = 1
    try:
        int(vel_0)
    except ValueError:
        print "Sorry, your velcoity input was not valid, please try again"
        flag = 0

a = g
b = float(vel_0)
c = -h
vel_f = -math.sqrt(b*b + 2.0*a*c)
t = (vel_f - b)/a
print "The object will take ", t, "s to hit the ground"
print "The final velocity will be ", vel_f, "m/s"