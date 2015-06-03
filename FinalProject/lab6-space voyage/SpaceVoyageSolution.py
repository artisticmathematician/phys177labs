"""
Created on Sat May 30 11:29:27 2015
Space Voyage Simulator: Earth and Moon
@author: Chris
"""

from __future__ import division
from visual import*
from visual.graph import*
import numpy

scene.y = 300
scene.width = 400
scene.height = 1000

#Constants I have provided for you, DO NOT CHANGE THESE VALUES!!!

G = 6.7e-11
mEarth = 6.7e24
mCraft = 15e3
mMoon = 7e22
deltaT = 390

#Objects you should modify for your program

Earth = sphere(pos = vector(0.0, 0.0, 0.0), radius = 6.4e6, color = color.cyan)
Moon = sphere(pos = vector(0.0, 4.0e8, 0.0), radius = 1.75e6, color = color.white)
Craft = sphere(pos = vector(0.0, -3.2e7, 0.0), radius = 1.0e6, color = color.red)
Trail = curve(color = color.red)    
pVector = arrow(color = color.green)
vCraft = vector(5077.5, 0, 0)

#Graph Information I have provided.

pCraft = vCraft*mCraft
t = 0
Kgraph = gcurve(color=color.red)
Ugraph = gcurve(color=color.blue)
KplusUgraph = gcurve(color=color.magenta)

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP

while t < 1000000:
    
   rate(250) 
   #Momentum arrow updated by the craft position
   pVector.pos = Craft.pos 
   #Earth-Craft position vector
   rE = Craft.pos-Earth.pos 
   #Magnitude of Earth-Craft position Vector
   rMagE = mag(rE) 
   #Unit vector for r in Earth-Craft direction
   rHatE = norm(rE) 
   #Magnitude of gravitational force from Earth-Craft system
   FGravMagE = G*mCraft*mEarth/(rMagE*rMagE)
   #Gravitational force from Earth-Craft system
   FGravE = -FGravMagE*rHatE 
   #Moon-Craft position vector
   rM = Craft.pos-Moon.pos 
   #Magnitude of Moon-Craft position vector r
   rMagM = mag(rM)
   #Unit vector for r in Moon-Craft direction
   rHatM = norm(rM) 
   #Magnitude of gravitational force from Moon-Craftsystem
   FGravMagM = G*mCraft*mMoon/(rMagM*rMagM)
   #Gravitational force from Moon-Craft system
   FGravM = -FGravMagM*rHatM 
   #Craft velocity
   vCraft = vCraft + (FGravE/mCraft)*deltaT + (FGravM/mCraft)*deltaT 
   #Craft momentum
   pCraft = pCraft + FGravE*deltaT + FGravM*deltaT 
   #Updates the direction the arrow points
   pVector.axis = 1*pCraft
   #Craft kinematic equation.
   Craft.pos = Craft.pos + (pCraft/mCraft)*deltaT
   #This leaves a trail behind the spacecraft
   Trail.append(pos = Craft.pos) 
   #Kinetic Energy
   K = 0.5*mCraft*mag(vCraft)**2 
   #Potential Energy
   U = numpy.dot(FGravE, rHatE)*rMagE + numpy.dot(FGravM, rHatM)*rMagM
   #Kinetic Energy plot
   Kgraph.plot(pos=(t,K))
   #Potential Energy Plot
   Ugraph.plot(pos=(t,U)) 
   #Total Mechanical Energy Plot
   KplusUgraph.plot(pos = (t, K + U)) 
   #Time increment
   t = t + deltaT