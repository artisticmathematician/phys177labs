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

#Objects you should modify for your program
Earth = sphere()
Moon = sphere()
Craft = sphere()
Trail = curve()    
pVector = arrow()
vCraft = vector(5077.5, 0, 0)

#Momentum: assign pcraft a mathematical statement for momentum. 
pCraft = x

#Graph Information I have provided.
Kgraph = x
Ugraph = x
KplusUgraph = x


while t < 1000000:
    #This will slow down the animation
    rate(250) 
    #Momentum arrow updated by the craft position

    #Earth-Craft position vector

    #Magnitude of Earth-Craft position Vector

    #Unit vector for r in Earth-Craft direction

    #Magnitude of gravitational force from Earth-Craft system

    #Gravitational force from Earth-Craft system

    #Moon-Craft position vector

    #Magnitude of Moon-Craft position vector r

    #Unit vector for r in Moon-Craft direction

    #Magnitude of gravitational force from Moon-Craftsystem

    #Gravitational force from Moon-Craft system

    #Craft velocity

    #Craft momentum

    #Updates the direction the arrow points

    #Craft kinematic equation.

    #This leaves a trail behind the spacecraft

    #Kinetic Energy

    #Potential Energy

    #Kinetic Energy plot

    #Potential Energy Plot

    #Total Mechanical Energy Plot

    #Time increment
    t = t + deltaT