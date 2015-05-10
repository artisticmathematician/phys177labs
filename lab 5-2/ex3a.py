"""
Created on Sat May 09 20:04:37 2015
This program is designed to examine sunspot data, it's function, and it's fft.
@author: Chris Cosio
"""

import matplotlib.pyplot as plt

filesun = open('sunspots.txt', 'r')
c = filesun.read().split()
filesun.close()
i = 0
month  = []
sunspots = []

while (i < len(c)):
    if (i%2 == 1 ):
        sunspots.append(float(c[i]))
    if (i%2 == 0):
        month.append(float(c[i]))
    i = i + 1

plt.scatter(month, sunspots)
plt.ylim(-100, 700)
plt.xlim(-100, 4250)
plt.title("Sunspots Every Month Since Jan. 1749")
plt.xlabel("Month")
plt.ylabel("Sunspots")
plt.show()

print "The cycle lengths seems to be around 130 months"




