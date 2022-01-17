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
coef1=nmp.zeros((n*n,n*n))
coef2=nmp.zeros((n*n,n*n))
x1=nmp.zeros(4);
y1=nmp.zeros(4);
x2=nmp.zeros(3);
y2=nmp.zeros(3);
place=0
for i in range (n):
    if(float(x[i])<float(T)):
        place+=1
    else:
        break;
i=0
for j in range(-2,2):
    x1[i]=x[place+j]
    y1[i]=y[place+j]
    i+=1
i=0
for j in range(-2,1):
    x2[i]=x[place+j]
    y2[i]=y[place+j]
    i+=1
for i in range(4):
    coef1[i][0]=y1[i];
for i in range(3):
    coef2[i][0]=y2[i];
coef1=DiffTable(x1, coef1, 4);
coef2=DiffTable(x2, coef2, 3);
print("The Cubic Newton result is: "+str(NInterpolation(T, x1, coef1, 4)));
print("The Cubic Lagrange result is: "+str(LInterpolation(x1, y1, 4,T)))
print("The Quadratic Newton result is: "+str(NInterpolation(T, x2, coef2, 3)));
print("The Quadratic Lagrange result is: "+str(LInterpolation(x2, y2, 3,T)));
print("The Relative Error is:  "+str(Error_checker(NInterpolation(T, x2, coef2, 3),NInterpolation(T, x1, coef1, 4)))+" %")
nmp.append(x,17)
nmp.append(y,NInterpolation(T, x1, coef1, 4))
plt.plot(x,y,'ro')
plt.show()