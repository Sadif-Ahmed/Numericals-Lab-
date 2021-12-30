# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:07:20 2021

@author: ahmed
"""
import numpy as nmp

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
    if(step!=1):
        if(showall):
            print("Partial Pivoting at Step "+str(step)+" :")
        temp=abs(A[step-1][0])
        pivot_row=step-1
        for i in range (pivot_row,len(A)):
            for j in range (len(A[0]-1)):
                if(temp<abs(A[i][j])):
                    temp=abs(A[i][j])
                    pivot_row=i
        if(pivot_row!=0):
                temp = nmp.zeros(len(A[0]))
                temp[:] = A[step-1,:]
                A[step-1,:] = A[pivot_row,:]
                A[pivot_row,:] = temp[:]
        if(showall):
            print_Mattrix(A)
    return A
             
def Elimination(A,pivot,showall):
    n=len(A)
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
    print("The results of the linear equations are:")
    return result


def GaussianElimination(A,B,pivot,showall):
    return Back_Subtraction(Elimination(Aug(A,B), pivot,showall))
                        
n=int(input())
Co_efficients=nmp.zeros((n,n))
values=nmp.zeros((n,1))
for i in range (n) :
        Co_efficients[i] = nmp.array(input().split())
for i in range (n):
    values[i][0]=nmp.array(input())
with nmp.printoptions(formatter={'float': '{: 0.4f}'.format}, suppress=True):
    print(GaussianElimination(Co_efficients, values, True , True))

