# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:42:09 2018

@author: rcostado
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

lAC=0.200
lAB=0.165
lBC=0.155
xEF=0.091
yEF=0.279
lCG=0.384
lBF=0.359
lBD=0.211
lDF=lBD-lBF
lFG=0.102
alpha=53.61*np.pi/180


R=0.325
l0=0.196
dl=0.2
m=1.5
P=m*9.81


def permutation(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t
    
def transvection(A,i,j,x):
    # si vecteur
    if type(A[0]) != list:
        A[i] = A[i] + x*A[j]
    else:
        n = len(A[0])
        for k in range(n):
            A[i][k] = A[i][k] + x*A[j][k]
    
def recherche_pivot(A, j0):
    n = len(A) 
    imax = j0 
    for i in range(j0+1, n):
        if abs(A[i][j0]) > abs(A[imax][j0]):
            imax = i
    return imax

def triangle(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x
    
def resolution_systeme(A0,b0):
    n = len(A)

    for i in range(n-1):
        i0 = recherche_pivot(A,i)
        permutation(A,i,i0)
        permutation(b,i,i0) 
        
        for k in range(i+1,n):
            x = A[k][i]/A[i][i]
            transvection(A,k,i,-x)
            transvection(b,k,i,-x) 
            
    return triangle(A,b)

Fv=[]

t=np.linspace(0,3,1000)
l=np.linspace(l0,l0+dl,1000)

#x[0]: theta2
#x[1]: theta3
#x[2]: theta4
#x[3]: theta5
#x[4]: lR

theta2,theta3,theta4,theta5,lR=[],[],[],[],[]

theta20=163*np.pi/180
theta20=2.844886680750757
theta30=170.34*np.pi/180
theta30=2.972993847847141
theta40=44.44*np.pi/180
theta40=0.77562431958628
theta50=100.23*np.pi/180
theta50=1.7493435092739165
lR0=0.309

for i in range(len(t)):

    def eq_geo(x):
        return [l[i]-lCG*np.sin(x[0])+lAC*np.sin(x[3])-R,
    -lCG*np.cos(x[0])+lBC*np.cos(x[3]+alpha)+lBF*np.cos(x[1]),
    -lCG*np.sin(x[0])+lBC*np.sin(x[3]+alpha)+lBF*np.sin(x[1])-lFG,
    xEF-x[4]*np.cos(x[2])+lDF*np.cos(x[1]),
    yEF-x[4]*np.sin(x[2])+lDF*np.sin(x[1])]

    x=op.fsolve(eq_geo,(theta20,theta30,theta40,theta50,lR0))
   
    theta20=x[0] 
    theta2.append(x[0])
    theta30=x[1]
    theta3.append(x[1])
    theta40=x[2]
    theta4.append(x[2])
    theta50=x[3]
    theta5.append(x[3])
    lR0=x[4] 
    lR.append(x[4])

    A=[[1,0,1,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0],
       [-np.sin(theta20),np.cos(theta20),0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,0,0],
        [0,0,0,0,-np.sin(theta50),np.cos(theta50),0,0,0,0,0,0],
         [0,0,-1,0,0,0,0,0,1,0,0,0],[0,0,0,-1,0,0,0,0,0,1,0,0],
    [0,0,-lAC*np.sin(theta40),lAC*np.cos(theta40),0,0,0,0,lAC*np.sin(theta40)-lBC,-lAC*np.cos(theta40),0,0],
     [0,0,0,0,0,0,-1,0,-1,0,1,0],[0,0,0,0,0,0,0,-1,0,-1,0,1],
    [0,0,0,0,0,0,lBD*np.sin(theta30),-lBD*np.cos(theta30),0,0,-lBF*np.sin(theta30),lBF*np.cos(theta30)]]
    
    b=[0,0,0,0,0,0,0,-P,0,0,0,0]
    x=resolution_systeme(A,b)
    Fv.append(np.sqrt(x[4]**2+x[5]**2))
    
plt.plot(t,Fv)
