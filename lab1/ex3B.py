"""
Lab Assignment 1-ex3A
Created on Fri Apr 10 16:03:31 2015
This program is a simulator for the amount of time it takes for a ball to
reach the bottom of a tower when thrown from the top of the tower.
@author: Chris Cosio
"""

import math
import matplotlib.pyplot as plt

flag = 0
h = 800.0
g = -9.81
t_list = [0,0,0,0,0,0,0,0,0,0]
v_list = [0,0,0,0,0,0,0,0,0,0]

while (flag == 0):
    vel_0min = raw_input("Enter an integer for intial minimum velocity: ")
    flag = 1
    try:
        int(vel_0min)
    except ValueError:
        print "Sorry, your velcoity input was not valid, please try again"
        flag = 0
        
flag = 0
while (flag == 0):
    vel_0max = raw_input("Enter an integer for intial maximum velocity: ")
    flag = 1
        
    try:
        int(vel_0max)
    except ValueError:
        print "Sorry, your velcoity input was not valid, please try again"
        flag = 0
        continue
    
    if (int(vel_0max) <= int(vel_0min) and flag == 1):
        print "Sorry, please enter a velocity that is higher than the intial value"
        flag = 0
        
a = g
c = -h
x = 0
increment = (float(vel_0min) - float(vel_0max))/10.0 
b = float(vel_0min) ##This is the velocity that is updated in the while loop
while (x < 10):
    v_list[x] = b
    vel_f = -math.sqrt(b*b + 2.0*a*c)
    t_list[x] = (vel_f - b)/a
    b = b + increment
    x = x + 1
    
time_list = '\n'.join(map(str, t_list))
vel_list = '\n'.join(map(str, v_list))
report = open("VelocityVsTime.txt","w")
report.write('Time incrments from the velocity verus time graph (s)\n\n' + time_list)
report.close()

plt.scatter(v_list, t_list)
plt.title("Intial velocity Vs Time")
plt.xlabel("Intial Velocity (m/s)")
plt.ylabel("Travel time (s)")
plt.show()
plt.savefig('vel0VStime.pdf')

print "The following graph is velocity vs travel time"