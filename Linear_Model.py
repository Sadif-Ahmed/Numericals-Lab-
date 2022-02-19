# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:35:02 2022

@author: ahmed
"""

import numpy as nmp;
import matplotlib.pyplot as plt;

fnc_x=lambda x:x
fnc_y=lambda y:y

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
def plot_graph(x_values, y_values, result):
   plt.title("Curve assumption based on given data")
   plt.xlabel("X-Values")
   plt.ylabel("Y-Values")
   plt.scatter(x_values, y_values)
   plt.plot(x_values, y_values, color="green")  # Provided Data
   plt.plot(x_values, res_fnc(x_values), color="blue")  # Computed Graph
   plt.show()

x_values=nmp.array([0.698132,0.95931,1.134464,1.570796,1.919862]);
y_values=nmp.array([0.188224,0.209138,0.230052,0.250965,0.313707]);
result=linear_model(x_values,y_values,5)
res_fnc=lambda x:result[0]+x*result[1]
plot_graph(x_values,y_values,result)
if(result[1]>0):
    print("y="+str(result[0])+"+ x * "+str(abs(result[1])))
else:
    print("y="+str(result[0])+"- x * "+str(abs(result[1])))

    
        