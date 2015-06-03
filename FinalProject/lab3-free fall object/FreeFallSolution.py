"""
Created on Sat May 23 22:50:03 2015
This is a program to simulate the free fall of a ball.
@author: Chris
"""
from __future__ import division
from visual import*
from visual.graph import*
import numpy 
#above are the libraries you will need for this program. I have included them 
#for you.

#Below define the mass as 0.5 and an acceleration vector that points only in 
#the y direction at -2.0 m/s^2
m = 0.5 
a = vector(0.0, -2.0, 0.0)

#Write two functions for PE and KE. Hint: use the numpy.dot(x,y) operation only 
#once in each definition.
def PE(y):
    pe = -m*numpy.dot(a, y)
    return pe

def KE(v):
    ke = 0.5*m*numpy.dot(v,v)
    return ke

#Define a position and velocity vector as well as time. Time starts at zero, 
#the object has zero velocity and the initial position is 50 meters above 
#ground.
h = vector(0, 50.0, 0)
v = vector(0.0, 0.0, 0.0)
t = 0.0

#Belowe you need to code two object, a flat sheet for the ground and a ball 
#that will drop. The radius of the ball should be 1.0 and the size of the sheet 
#should be 20x20x2. Lastly, the sheet should be at the orgin and the ball 
#should be 50 m above the sheet
ball = sphere(pos = h, radius = 1.0, color = color.red)
track = box(pos = vector(0, 0, 0), size = (20, 2, 20), color = color.green)

#This is the code for the graphs that I have included, do not modify this code.
Kgraph = gcurve(color = color.red)
Ugraph = gcurve(color = color.blue)
KplusUgraph = gcurve(color = color.magenta)

#This is the loop you will program. Run the loop for 7 seconds and increment 
#the time by 0.1 seconds. I set the rate alread, so don't modify that. I have
#included most of the code for your graphs. You must add the missing components
#to make the graphs work. Hint: use your functions somehow to update the graphs
while t < 7.2:
    rate(10)
    ball.pos = h + 0.5*a*t*t
    #Kinetic Energy plot
    K = KE(v)
    Kgraph.plot(pos = (t,K))
    #Potential Energy Plot
    U = PE(ball.pos)
    Ugraph.plot(pos = (t,U)) 
    #Total Mechanical Energy Plot
    KplusUgraph.plot(pos = (t, K + U)) 
    v = v + a*0.1
    t = t + 0.1
    