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
def Interpolation(value, x, y, n): 
  
    res = y[0][0]; 
  
    for i in range(1, n):
        res = res + (product(i, value, x) * y[0][i]); 
      
    return res; 
def Error_checker(a,b):
    return (abs((a-b)/a))*100
     
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
plt.plot(x,y)
coef=DiffTable(x, coef, n);
print("The result is:"+str(Interpolation(T, x, coef, n)));
#For quadratic interpolation
x1=nmp.zeros(4)
y1=nmp.zeros(4)
for i in range (n):
    if(float(x[i])/float(T)>1):
        temp=i
        break
for i in range(-1,3):
    x1[i+1]=x[temp+i]
    y1[i+1]=y[temp+1]
coef1=nmp.zeros((16,16))
for i in range(4):
    coef1[i][0]=y1[i];    
coef1=DiffTable(x1, coef1, 4);
print("The result(2) is:"+str(Interpolation(T, x1, coef1, 4)));
print("The Error is  "+str(Error_checker(Interpolation(T, x1, coef1, 4),Interpolation(T, x, coef, n)))+" %")