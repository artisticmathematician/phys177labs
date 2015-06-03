"""
Created on Sat May 30 11:29:27 2015
Space Voyage Simulator: Earth and Moon
@author: Chris
"""

from __future__ import division
from visual import*
from visual.graph import*
import numpy as np

#This will set the default window size, do not change!
scene.y = 300
scene.width = 400
scene.height = 1000

#Constants I have provided for you, DO NOT CHANGE THESE VALUES!!!
G = 6.7e-11
mEarth = 6.7e24
mCraft = 15e3
mMoon = 7e22
deltaT = 390
t = 0

#This variable will be used as a placeholder for spots in your code that must
#be writen over and updated.
x = 1.0
y = 1.0
z = 1.0

#Objects you should modify for your program
Earth = sphere()
Moon = sphere()
Craft = sphere()
Trail = curve()    
pVector = arrow()
vCraft = vector(5077.5, 0, 0)

#Momentum: assign pcraft a mathematical statement for momentum. Hint: x*y
pCraft = x

#Graph Information I have provided.
Kgraph = gcurve(color=color.red)
Ugraph = gcurve(color=color.blue)
KplusUgraph = gcurve(color=color.magenta)

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP

while t < 1000000:
    #This will slow down the animation
    rate(250) 
    #Momentum arrow updated by the craft position
    pVector.pos = (x, y, z) 
    #Earth-Craft position vector
    rE = x
    #Magnitude of Earth-Craft position Vector
    rMagE =  x
    #Unit vector for r in Earth-Craft direction
    rHatE = x
    #Magnitude of gravitational force from Earth-Craft system
    FGravMagE = x
    #Gravitational force from Earth-Craft system
    FGravE = x 
    #Moon-Craft position vector
    rM = x 
    #Magnitude of Moon-Craft position vector r
    rMagM = x
    #Unit vector for r in Moon-Craft direction
    rHatM = x 
    #Magnitude of gravitational force from Moon-Craftsystem
    FGravMagM = x
    #Gravitational force from Moon-Craft system
    FGravM = x
    #Craft velocity
    vCraft = x 
    #Craft momentum
    pCraft = x 
    #Updates the direction the arrow points
    pVector.axis = 1*(x, y, z)
    #Craft kinematic equation.
    Craft.pos = (x, y, z)
    #This leaves a trail behind the spacecraft
    Trail.append(pos = (x, y, z)) 
    #Kinetic Energy
    K = x 
    #Potential Energy
    U = x
    #Kinetic Energy plot
    Kgraph.plot(pos=(t,x))
    #Potential Energy Plot
    Ugraph.plot(pos=(t,x)) 
    #Total Mechanical Energy Plot
    KplusUgraph.plot(pos = (t, x)) 
    #Time increment
    t = t + deltaT