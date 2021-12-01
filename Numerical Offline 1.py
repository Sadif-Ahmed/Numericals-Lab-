# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as nmp
import matplotlib.pyplot as plt
fnc= lambda x : x*x*x - 0.18*x*x + 0.0004572
x_values=nmp.arange(-1,1,0.01);
y_values=fnc(x_values)
y_axis=nmp.zeros(len(y_values))
x_axis=nmp.zeros(len(y_values))
#print(x_values)
#print(y_values)
plt.plot(x_values,y_axis)
plt.plot(x_axis,x_values)
plt.plot(x_values,y_values)

def Error_checker(a,b):
    return (abs((a-b)/a))*100
    
def bisector(xl,xu,app_err,max_iter):
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        for i in range(max_iter-5):
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
result=bisector(0.04,0.07,0.5,100)
print(result)
def error_table(xl,xu,max_iter):
    errors=[];
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        for i in range(max_iter-5):
            if(fnc(xl)*fnc(xm)<0):
                xu=xm
                xm=(xl+xu)/2  
                errors.append(Error_checker(xm, xu))
            if(fnc(xm)*fnc(xu)<0):
                xl=xm
                xm=(xl+xu)/2
                errors.append(Error_checker(xm, xu))
    for i in range(len(errors)):
        print("Iterartion No. "+str(i+1)+"  "+str(errors[i]))
    

error_table(0.04,0.07,20)
        
    
            
           
   