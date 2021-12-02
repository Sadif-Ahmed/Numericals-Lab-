# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:02:31 2021

@author: ahmed
"""

import numpy as nmp
import matplotlib.pyplot as plt
fnc= lambda x : x*x*x - 0.18*x*x + 0.0004752
x_values=nmp.arange(0,0.15,0.01);
y_values=fnc(x_values)
axis=nmp.zeros(len(y_values))
#print(x_values)
#print(y_values)
plt.plot(x_values,y_values)
plt.plot(x_values,axis)
plt.title('The graph to visualize f(x) and find approximate root')
def Error_checker(a,b):
    return (abs((a-b)/a))*100
    
def bisector(xl,xu,app_err,max_iter):
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        for i in range(max_iter-6):
            if(fnc(xl)*fnc(xm)<0):
                xu=xm
                xm=(xl+xu)/2  
                if(Error_checker(xm, xu)<=app_err): 
                    return xm
            if(fnc(xm)*fnc(xu)<0):
                xl=xm
                xm=(xl+xu)/2
                if(Error_checker(xm, xl)<=app_err):
                    return xm
            if(fnc(xm)*fnc(xl)==0):
                return xm
    else:
        return 0;
def error_table(xl,xu,max_iter):
    errors=[];
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        errors.append(-1)
        for i in range(max_iter-6):
            if(fnc(xl)*fnc(xm)<0):
                xu=xm
                xm=(xl+xu)/2  
                errors.append(Error_checker(xm, xu))
            if(fnc(xm)*fnc(xu)<0):
                xl=xm
                xm=(xl+xu)/2
                errors.append(Error_checker(xm, xl))
    for i in range(len(errors)):
        print("Iterartion No. "+str(i+1)+"  "+str(errors[i]))
result=bisector(0, 0.08,0.05, 20)
error_table(0, 0.08, 20)
print("The root of the equation is:  "+str(result))