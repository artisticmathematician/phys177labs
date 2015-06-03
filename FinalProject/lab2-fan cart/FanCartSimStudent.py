"""
Created on Sat May 23 18:57:09 2015
This is the broken code for the fan cart simulation lab
@author: Chris
"""


"""This is a buggy program code I have provided you. I will indicate where things
need to be changed with these grey comments. You can also write comments to 
help remind you of what things do. Simply type a "#" before you start a comment
and anything after it will be just normal text that the program does not read.
if you need to make an extended comment, use a new # for a new line or use three
" in a row to start the comment and three " in a row to end the comment"""

#The two lines below are libraries and are already correctly added.
#Libraries allow you to inport functions or attributes not normally included
#in your programming enviroment. 
from __future__ import division
from visual import*

#The code below has some physics mistakes and is missing values. Use the 
#information provided on the handout to help complete the code. Assume no new
#variables need to be made and all changes will on occur on the assignment side
#of the variables.

mcart = 0.0 #mass in kilograms
vcart = (0.0, 0, 0.0) #initial velocity of the cart
pcart = mcart + vcart #momentum of cart
t = "time starts at?" #initial time
deltat = 0.01 #change in time in seconds
fEx = vector()#External force acting upon the cart
print('cart momentum=',pcart)

#This code is for the visualization part of your program. I have removed the 
#attributes from the cart and track, you must put them back into this code
#based off of the values I included in the handout.
track = box()
cart = box()

#This loop will change time, momentum, and position incrementally. It has two
#physics errors. Using our recent lessons on impulse and momentum, correct
#the code within the loop below
while t<=15.2:
    rate(100)
    pcart = pcart #Change in momentum
    cart.pos = cart.pos  #Change in cart position
    t = t + deltat
print('end of program')