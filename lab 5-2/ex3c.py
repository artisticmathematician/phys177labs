"""
Created on Sat May 09 20:04:37 2015
This program is designed to examine sunspot data, it's function, and it's fft.
@author: Chris Cosio
"""

import scipy
import numpy as np
import math
import matplotlib.pyplot as plt

filesun = open('sunspots.txt', 'r')
c = filesun.read().split()
filesun.close()
i = 0
j = 0
k = 0
month  = []
sunspots = []
dataset = []
Asquared = []

while (i < len(c)):
    if (i%2 == 1 ):
        sunspots.append(float(c[i]))
    if (i%2 == 0):
        month.append(float(c[i]))
    i = i + 1
    
while (j < len(sunspots)):
    dataset.append((month[j], sunspots[j]))
    j = j + 1

fft = np.fft.fft(sunspots)
fftconj = np.conjugate(fft)

while (k < len(fft)):
    Asquared.append(math.pow(math.sqrt(fft[k]*fftconj[k]), 2))
    k = k + 1

plt.scatter(month, fft)
plt.ylim(-100, 15000)
plt.xlim(-100, 8000)
plt.title("A graph of amplitudes squared")
plt.xlabel("Amplitude Squared")
plt.ylabel("Counts")
plt.show()

str1 = "The amplitude value for the non zero K is around 3000."
str2 = "The 3000 \nterm for amplitude corresponds to the sine"
str3 = "term with the period\n"

print str1, str2, str3, "of 130 days"




