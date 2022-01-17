# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 20:33:45 2022

@author: ahmed
"""
import numpy as nmp
import matplotlib.pyplot as plt
def DiffTable(x, coef, n):
    for i in range(1, n): 
        for j in range(n - i): 
            coef[j][i] = ((coef[j][i - 1] - coef[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return coef;
def product(i, value, x): 
    prod = 1; 
    for j in range(i): 
        prod=prod*(float(value)-float(x[j]))
    return prod; 
def NInterpolation(value, x, y, n): 
  
    res = y[0][0]; 
  
    for i in range(1, n):
        res = res + (product(i, value, x) * y[0][i]); 
      
    return res; 
def Error_checker(a,b):
    return (abs((a-b)/a))*100
def LInterpolation(x,y,n,xp):
    res=0
    for i in range(n):
        temp = 1.00
        for j in range(n):
            if i != j:
                temp = temp * ((float(xp) - float(x[j]))/(float(x[i]) - float(x[j])))
    
        res = res + temp * float(y[i])
    return res

f= open("gene.txt","r")
array =[]
for line in f: # read rest of lines
        array.append([float(x) for x in line.split()])
T=input();
n=len(array)
x=nmp.zeros(n);
y=nmp.zeros(n);
for i in range(n):
    x[i]=array[i][0]
    y[i]=array[i][1]
coef=nmp.zeros((n*n,n*n))
for i in range(n):
    coef[i][0]=y[i];
coef=DiffTable(x, coef, n);
print("The Newton result is:"+str(NInterpolation(T, x, coef, n)));
print("The Lagrange result is:"+str(LInterpolation(x, y, n,T)));
#For quadratic interpolation
x1=nmp.zeros(3)
y1=nmp.zeros(3)
x1[0]=16
y1[0]=6.7
x1[1]=20
y1[1]=5.5
x1[2]=24
y1[2]=4.3
coef1=nmp.zeros((16,16))
for i in range(3):
    coef1[i][0]=y1[i];    
coef1=DiffTable(x1, coef1, 3);
print("The Quadratic newton result is:"+str(NInterpolation(T, x1, coef1, 3)));
print("The Quadratic lagrange result is:"+str(LInterpolation(x1, y1, 3,17)));
print("The Error is  "+str(Error_checker(NInterpolation(T, x1, coef1, 3),NInterpolation(T, x, coef, n)))+" %")

plt.plot(x,y)
#plt.plot(T,Interpolation(T, x, coef, n),'g*')
plt.show()