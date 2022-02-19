# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:05:03 2022

@author: ahmed
"""

import numpy as nmp;
import math;
import matplotlib.pyplot as plt

fnc_x=lambda x:x
fnc_y=lambda y:math.log(y)


def plot_graph(x_values, y_values, result):
   plt.title("Curve assumption based on given data")
   plt.xlabel("X-Values")
   plt.ylabel("Y-Values")
   plt.scatter(x_values, y_values)
   plt.plot(x_values, y_values, color="green")  # Provided Data
   plt.plot(x_values, res_fnc(x_values), color="blue")  # Computed Graph
   plt.show()

def linear_model(x,y,n):
    sum_x=0
    sum_y=0
    sum_xy=0
    sum_s_x=0
    for i in range (n):
        sum_x=sum_x+fnc_x(x[i])
        sum_y=sum_y+fnc_y(y[i])
        sum_xy=sum_xy+fnc_x(x[i])*fnc_y(y[i])
        sum_s_x=sum_s_x+pow(fnc_x(x[i]),2)
        
    sum_x_y=sum_x*sum_y
    b=(n*sum_xy-sum_x_y)/(n*sum_s_x-pow(sum_x,2))
    a=(sum_y/n)-b*(sum_x/n)
    return a,b
def trans_exp(result):
    a_real=nmp.exp(result[0])
    b_real=result[1]
    return a_real,b_real;
x_values=nmp.array([0, .01, .03, .05, .07, .09, .11, .13, .15, .17, .19, .21])
y_values=nmp.array([1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
result=trans_exp(linear_model(x_values, y_values, 12))
res_fnc= lambda x:result[0] * nmp.exp(result[1]*x)
plot_graph(x_values, y_values, result)
print("y = "+str(result[0])+"e^x"+str(result[1]));