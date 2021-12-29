# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:26:16 2021

@author: ahmed
"""

import numpy as nmp
import matplotlib.pyplot as plt
fnc= lambda x : x*x*x - 0.18*x*x + 0.0004752
fnc1=  lambda x: 3*x*x - 2*0.18*x
x_values=nmp.arange(0,0.15,0.01);
y_values=fnc(x_values)
#axis=nmp.zeros(len(y_values))
#print(x_values)
#print(y_values)
plt.plot(x_values,y_values,marker="o")
plt.axhline(y=0)
plt.axvline(x=0)
plt.title('The graph to visualize f(x) and find approximate root')
def Error_checker(a,b):
    return (abs((a-b)/a))*100
    
def bisector(xl,xu,app_err,max_iter):
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        err=99.99
        iter=1
        while((err>app_err) or (iter<=max_iter)):
            if(fnc(xl)*fnc(xm)<0):
                xu=xm
                xm=(xl+xu)/2  
                err=Error_checker(xm, xu)
                iter+=1
            elif(fnc(xm)*fnc(xu)<0):
                xl=xm
                xm=(xl+xu)/2
                err=Error_checker(xm, xl)
                iter+=1
            else:
                break
    return xm
def error_table(xl,xu,max_iter):
    errors=[];
    iter=1;
    if(fnc(xl)*fnc(xu)<0):
        xm=(xl+xu)/2 
        while(iter<max_iter):
            if(fnc(xl)*fnc(xm)<0):
                xu=xm
                xm=(xl+xu)/2  
                errors.append(Error_checker(xm, xu))
                iter+=1
            elif(fnc(xm)*fnc(xu)<0):
                xl=xm
                xm=(xl+xu)/2
                errors.append(Error_checker(xm, xl))
                iter+=1
    print("Iterations     "+" "+"   "+"Expected Realative Approximate Errors")
    print("Iterartion No. "+str(1)+"   "+"No error can be calculated")
    for i in range(len(errors)):
        if(i<8):
            print("Iterartion No. "+str(i+2)+"   "+str(errors[i]))
        else:
            print("Iterartion No. "+str(i+2)+"  "+str(errors[i]))

def newton(x1,max_iter,max_error):
    iter=0;
    app_err=99.99;
    while(app_err>=max_error or iter<max_iter):
        temp=x1;
        if(fnc1(x1)==0):
            break
        x1=x1-(fnc(x1)/fnc1(x1))
        app_err=Error_checker(x1, temp)
        iter+=1;
    return x1;
            
#result=bisector(0.06,0.08,0.5, 100)
result=newton(0.05, 1000, 0.05)      
#error_table(0.06, 0.08, 20)
print("The root of the equation is:  "+str(result))