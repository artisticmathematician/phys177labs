"""
Created on Sat May 30 11:29:27 2015
Space Voyage Simulator: Earth and Moon
@author: Chris
"""
from __future__ import division
from visual import*
from visual.graph import*
import numpy

scene.y = 100
scene.width = 1000
scene.height = 1000

#Constants I have provided for you, DO NOT CHANGE THESE VALUES!!!

G = 6.7e-11
mEarth = 6.7e24
mSatellite = 15e3
deltaT = 390

#Objects you should modify for your program

Earth = sphere(pos = vector(0.0, 0.0, 0.0), radius = 6.4e6, color = color.cyan)
Satellite = sphere(pos = vector(0.0, -4.2e7, 0.0), radius = 1.0e6, color = color.red)
Trail = curve(color = color.red)    
pVector = arrow(color = color.green)
vSatellite = vector(4000, 0, 0)

#Graph Information I have provided.

pSatellite = vSatellite*mSatellite
t = 0

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP

while t < 1000000:
   rate(250) 
   #Momentum arrow updated by the satelite position
   pVector.pos = Satellite.pos 
   #Earth-satelite position vector
   rE = Satellite.pos - Earth.pos 
   #Magnitude of Earth-satelite position Vector
   rMagE = mag(rE) 
   #Unit vector for r in Earth-satelite direction
   rHatE = norm(rE) 
   #Magnitude of gravitational force from Earth-satelite system
   FGravMagE = G*mSatellite*mEarth/(rMagE*rMagE)
   #Gravitational force from Earth-satelite system
   FGravE = -FGravMagE*rHatE 
   #Craft velocity
   vSatellite = vSatellite + (FGravE/mSatellite)*deltaT
   #Craft momentum
   pSatellite = pSatellite + FGravE*deltaT
   #Updates the direction the arrow points
   pVector.axis = 1*pSatellite
   #Satelite kinematic equation.
   Satellite.pos = Satellite.pos + (pSatellite/mSatellite)*deltaT
   #This leaves a trail behind the spacecraft
   Trail.append(pos = Satellite.pos) 
   t = t + deltaT