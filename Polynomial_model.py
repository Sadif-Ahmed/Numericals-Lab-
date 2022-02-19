# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:07:30 2022

@author: ahmed
"""

import numpy as nmp


t = [80, 40, -40, -120, -200, -280, -340]
alpha = [6.47e-6, 6.24e-6, 5.72e-6, 5.09e-6, 4.30e-6, 3.33e-6, 2.45e-6]


def powerSum(n, power, base):
    sum =0
    for i in range(n):
        sum += pow(base[i], power)

    return sum


def powerSum2(n,power1,power2,base1,base2):
    sum = 0
    for i in range(n):
        sum += pow(base1[i],power1)*pow(base2[i],power2)
    return sum

def print_Mattrix(Mat):
    Co_eff=nmp.zeros((len(Mat),len(Mat)))
    Values=nmp.zeros((len(Mat),1))
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            Co_eff[i][j]=Mat[i][j]
    for i in range(len(Mat)):
        Values[i][0]=Mat[i][len(Mat)]
    with nmp.printoptions(formatter={'float': '{: 0.4f}'.format}, suppress=True):
        print("The Co-efficient Mattrix: ")
        print(Co_eff)
        print("The Constant Mattrix: ")
        print(Values)
             
def Aug(A,B):
    Ag=nmp.zeros((len(A),len(A)+1))
    for i in range (len(A)):
        for j in range (len(A)):
            Ag[i][j]=A[i][j]
    for i in range (len(B)):
        Ag[i][len(B)]=B[i][0]
    return Ag
def pivot_func(A,step,showall):
    if(showall):
        print("Partial Pivoting at the Start of Step "+str(step)+" :")
    temp=abs(A[step-1][step-1])
    pivot_row=step-1
    for i in range (step-1,len(A)):
        if nmp.abs(A[i,step-1])>temp:
           temp=nmp.abs(A[i,step-1])
           pivot_row = i
    if(pivot_row!=0):
            temp = nmp.zeros(len(A[0]))
            temp[:] = A[step-1,:]
            A[step-1,:] = A[pivot_row,:]
            A[pivot_row,:] = temp[:]
    if(showall):
        if(pivot_row!=step-1):
            print_Mattrix(A)
        else:
            print("Pivoting Not Necessary at this step")
    return A
             
def Elimination(A,pivot,showall):
    n=len(A)
    if(showall):
        print("The Start of Elimination Process:")
        print_Mattrix(A)
    for i in range(n-1):
        if A[i][i] == 0.0:
            print('Division By Zero')
        if(pivot):
            pivot_func(A,i+1,showall)
        if(showall):
            print("Elimination Step "+str(i+1)+" : ")
        for j in range(i+1, n):
            r = A[j][i]/A[i][i]
            
            for k in range(n+1):
                A[j][k] = A[j][k] - r * A[i][k]
            if(showall):
                print_Mattrix(A)
    return A
def Back_Subtraction(A):
    n=len(A)
    result=nmp.zeros((n,1))

    result[n-1]=A[n-1,n]/A[n-1,n-1]
    for i in range(int(n-1),int(-1),int(-1)):
        for j in range(int(i+1),int(n)):
            A[i,n] = A[i,n]-A[i,j]*result[j]

        result[i] = A[i,n]/A[i,i]
   # print("The results of the linear equations are:")
    return result


def GaussianElimination(A,B,pivot,showall):
    return Back_Subtraction(Elimination(Aug(A,B), pivot,showall))
                        

def solve(n):
    #print(powerSum(7, 3))
    c11 = n
    c12 = c21 = powerSum(7, 1, t)
    c13 = c22 = c31 = powerSum(7, 2, t)
    c23 = c32 = powerSum(7, 3, t)
    c33 = powerSum(7, 4, t)

    b1 = powerSum(7, 1, alpha)
    b2 = powerSum2(7, 1, 1, t, alpha)
    b3 = powerSum2(7, 2, 1, t, alpha)

    a = nmp.array([[c11, c12, c13],
                 [c21, c22, c23],
                 [c31, c32, c33]])

    b = nmp.array([[b1], [b2], [b3]])

    x = GaussianElimination(a, b, True, False)
    print(x)
    

solve(7)