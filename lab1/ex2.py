"""
Lab Assignment 1-ex2
Created on Fri Apr 10 16:03:31 2015
This program computes grades from a already known set of data
@author: Chris Cosio
"""

import matplotlib.pyplot as plt

homework = [10,10,8,9.5,3,9,0,6]
midterm = [10,10,10,10,8,5,10,7]
final = [9,10,10,6,10,6,8,9]
grades = [0,0,0,0,0,0,0,0]
x = 0
fail = 0
A_plus = 0

while (x < 8):
    grades[x] = (homework[x] + midterm[x] + final[x])/3
    if(grades[x] > 9.5):
        A_plus = A_plus + 1
    if(grades[x] < 6):
        fail = fail + 1
    x = x + 1

report_list = '\n'.join(map(str, grades))
report = open("gradeReport.txt","w")
report.write('Final Grades\n\n' + report_list)
report.close()
 
plt.hist(grades)
plt.ylim(0,3)
plt.xlim(5,12)
plt.title("Histogram of grades")
plt.xlabel("Grade")
plt.ylabel("Number of students")
plt.show()
plt.savefig('GradePlot.pdf')

print "Number of  students who have a grade less than a D:", fail
print "Number of A+ students:", A_plus  
 


    