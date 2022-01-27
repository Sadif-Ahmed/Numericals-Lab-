# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:49:20 2022

@author: ahmed
"""

import numpy as nmp
import matplotlib.pyplot as plt

def Error_checker(a,b):
    return (abs((a-b)/a))*100

fnc= lambda x : ((6.73*x+6.725e-8+7.26e-4*5e-4)/(3.62e-12*x+3.908e-8*x*5e-4))

def Trapeziodal_Integration(a,b,n):
    h=(b-a)/n
    result=(fnc(a)+fnc(b))*h
    for i in range(1,n):
        result=result+2*h*fnc(a+i*h)
    return result/2
def Simpsons_Integration(a,b,n):
    n=n*2
    h=(b-a)/n
    result=(fnc(a)+fnc(b))*h
    for i in range(1,n):
        if(i%2==1):
            result=result+4*h*fnc(a+i*h)
        else:
            result=result+2*h*fnc(a+i*h)
    return result/3
#main starts here
x1=1.22e-4
x2=x1*(50/100)
print("Give the number of intervals: ")
n=int(input())
#Answer To The Question 1
print("Trapezoidal Integral " +"is: "+str(Trapeziodal_Integration(x1, x2, n)*(-1)))
print("No. of intervals"+"\t \t"+"Result"+"\t \t \t \t"+"Absolute Approximate Relative Error")
for i in range(1,6):
    if(i==1):
        print(str(i)+"\t \t \t \t \t"+str(Trapeziodal_Integration(x1, x2, i)*(-1))+"\t \t \t"+"Not Applicable")
    else:
        print(str(i)+"\t \t \t \t \t"+(str(Trapeziodal_Integration(x1, x2, i)*(-1))+"\t \t \t"+(str(Error_checker(Trapeziodal_Integration(x1, x2, i),Trapeziodal_Integration(x1, x2, i-1))))))
#Answer To The Question 2
print("Simpsons' 1/3 Integral "+"is: "+str(Simpsons_Integration(x1, x2, n)*(-1)))
print("No. of intervals"+"\t \t"+"Result"+"\t \t \t \t"+"Absolute Approximate Relative Error")
for i in range(1,6):
    if(i==1):
        print(str(i)+"\t \t \t \t \t"+str(Simpsons_Integration(x1, x2, i)*(-1))+"\t \t \t"+"Not Applicable")
    else:
        print(str(i)+"\t \t \t \t \t"+(str(Simpsons_Integration(x1, x2, i)*(-1))+"\t \t \t"+(str(Error_checker(Simpsons_Integration(x1, x2, i),Trapeziodal_Integration(x1, x2, i-1))))))
#Answer To The Question 3
x_values=nmp.array([1.22e-4,1.20e-4,1.0e-4,0.8e-4,0.6e-4,0.4e-4,0.2e-4])
y_values=nmp.zeros((nmp.size(x_values)))
for i in range (1,nmp.size(x_values)+1):
    y_values[i-1]=(Simpsons_Integration(x1, x_values[i-1], 10)*(-1))
    
plt.plot(x_values,y_values, marker = 'o')
plt.xlabel("Oxygen concentration (moles/cm^3)")
plt.ylabel("Time (seconds)")
plt.title("Consumption of oxygen over time in methanol-based fuel cell")
plt.grid()
plt.show()        