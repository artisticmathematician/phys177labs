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
m = 
a = 

#Write two functions for PE and KE. Hint: use the numpy.dot(x,y) operation only 
#once in each definition.
def PE(y):
    pe = 
    return pe

def KE(v):
    ke = 
    return ke

#Define a position and velocity vector as well as time. Time starts at zero, 
#the object has zero velocity and the initial position is 50 meters above 
#ground.
h = 
v = 
t = 

#Belowe you need to code two object, a flat sheet for the ground and a ball 
#that will drop. The radius of the ball should be 1.0 and the size of the sheet 
#should be 20x20x2. Lastly, the sheet should be at the orgin and the ball 
#should be 50 m above the sheet
ball = 
track = 

#This is the code for the graphs that I have included, do not modify this code.
Kgraph = gcurve(color = color.red)
Ugraph = gcurve(color = color.blue)
KplusUgraph = gcurve(color = color.magenta)

#This is the loop you will program. Run the loop for 7 seconds and increment 
#the time by 0.1 seconds. Don't forget to increment the velocity as well. The
#way you can increment velocity is using the equation vf = vi + at. I set the 
#rate alread, so don't modify that. I have included most of the code for your 
#graphs. You must add the missing components to make the graphs work. Hint: use 
#your functions somehow to update the graphs.
while t < 7.2:
    rate(50)
    ball.pos = 
    #Kinetic Energy plot, make sure to replace the XXXXXX term
    K = 
    Kgraph.plot(pos = (t,XXXXXX))
    #Potential Energy Plot, make sure to replace the XXXXXX term
    U = PE(ball.pos)
    Ugraph.plot(pos = (t,XXXXXX)) 
    #Total Mechanical Energy Plot
    KplusUgraph.plot(pos = (t, K + U)) 
    v = 
    t =
    