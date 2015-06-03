"""
Created on Sat May 23 18:57:09 2015
This is the working fan cart simulation for lab 2
@author: Chris
"""
import numpy as np
import matplotlib.pyplot as plt
#Above are the libraries you will need to import for this program. 

#An array for time, use map(float, array) to convert you list 
tfile = open("timeData.txt", "r")
tlist = map(float, tfile.read().split())
tfile.close()
#An array for velocity, use map(float, array) to convert you list 
vfile = open("velocityData.txt","r")
vlist = map(float, vfile.read().split())
vfile.close()

#Assign variables the size of each list to help you in your calculations
sizeV = len(vlist)
sizeT = len(tlist)

#Write your code here to calculate acceleration and the standard deviation.
accAVG = (vlist[sizeV - 1] - vlist[0])/tlist[sizeT - 1]
STD = np.std(vlist)

#Write your print statments here that output average acceleration and std.
print "The average acceleration is: ", accAVG
print "The std value for velocity is: ", STD

#This is the code for showing your plot, do not modify anything else other than
#locations where you see XXXXXX
plt.scatter(vlist, tlist)
plt.title("Intial velocity Vs Time")
plt.xlabel("Intial Velocity (m/s)")
plt.ylabel("Travel time (s)")
plt.show()
