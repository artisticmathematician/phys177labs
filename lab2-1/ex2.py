"""
Created on Sat Apr 11 13:57:42 2015
This program is desined to explore integration via simpsoms and 
trapazoidal rule.
@author: Chris Cosio
"""

import math
import matplotlib.pyplot as plt

def trap_rule (list):
    i = len(list)
    j = 0 
    area = 0
    dx = (list[j+1][0] - list[j][0])
    k = dx/2
    while (j < i - 1):
        if((j != 0) and (j != (i - 2))):
            c = 2
        if((j == 0) or (j == (i - 2))):
            c = 1
        area = area + c*k*list[j][1]
        j = j + 1
    return (area)

def simp_rule (list):
    i = len(list)
    delx = list[1][0] - list[0][0]
    j = 0
    area = 0
    while (j < i - 1):
        if ((j%2 != 0) and (j != 0) and j != (i - 2)):
            c = 4
        if ((j%2 == 0) and (j != 0) and j != (i - 2)):
            c = 2
        if (j == 0) or j == (i - 2):
            c = 1
        area = area + c*(delx/3)*list[j][1]
        j = j + 1
    return (area)


fileVel = open('velocities.txt', 'r')
v = fileVel.read().split()
fileVel.close()
dataT = []
dataV = []
data = []
i = len(v)
j = 0
k = 0
num = 0

while (j < i):
    if ((j == 0) or (j%2 == 0)):
        num = float(v[j])
        dataT.append([num])
    if (j%2 != 0):
        num = float(v[j])
        dataV.append([num])
    if (j%2 != 0):
        k = k +1
    j = j + 1
    
i = len(dataT)
j = 0
while (j < i):
    t = dataT[j]
    v = dataV[j]
    temp = t + v
    data.append(temp)
    j = j + 1
    
### I did not know how to derive the position function from using the value
### obtained from trapezoidal or simpsom rules. I found the cosine function
### from the given velocity data.
    
position = []
x = 0
j = 0
while (j < 101):
    x = -(45/3.14)*math.cos((3.14/45)*j)
    position.append(x)
    j = j + 1
print range

report = open("Integrated_Position.txt","w")
intro1 = "Integration by trapeziod rule and simpsons rule respectively"
intro2 = " (unit in meters):\n"
intro = intro1 + intro2
report.write(intro + str(trap_rule(data)) + '\t' + str(simp_rule(data)))
report.close()
print "trap rule: ", trap_rule(data), "\nsimp rule: ", simp_rule(data)

plt.subplot(2, 1, 2).scatter(dataT, dataV)
plt.subplot(2, 1, 1).scatter(dataT, position)

g = plt.subplot(2, 1, 2)
g.set_title("Velocity Vs Time")
g.set_xlabel("Time (s)")
g.set_ylabel("Velocity(m/s)")

g = plt.subplot(2, 1, 1)
g.set_title("Position Vs Time")
g.set_xlabel("Time (s)")
g.set_ylabel("Position (m)")

plt.tight_layout()
plt.savefig('pos&velGraph.pdf')
plt.show()






