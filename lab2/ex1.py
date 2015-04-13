"""
Created on Sat Apr 11 13:57:42 2015
This program is desined to explore integration via simpsoms and 
trapazoidal rule.
@author: Chris Cosio
"""

### I used the polynomial expression to define both my trapezoid and simpsom 
### rules. 

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


