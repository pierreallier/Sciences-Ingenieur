# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:16:49 2017

@author: costa
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=4.25*2*np.pi/360     # angle alpha en rd
b=5.885*2*np.pi/360    # angle béta en rd
rf=0.270             # rayon sur plate forme fixe
rm=0.195             # rayon sur plate forme mobile
h=0.276              # hauteur de référence (hauteur lorsque les vérins sont rentrés)

def longueurs(x,y,z,theta1,theta2,theta3):
    xf=np.zeros(6)
    yf=np.zeros(6)
    zf=np.zeros(6)
    xm=np.zeros(6)
    ym=np.zeros(6)
    zm=np.zeros(6)
    alpha=np.zeros(6)
    beta=np.zeros(6)

    u=0
    v=1
    
    #Calcul des angles alpha
    for i in range(1,7):
        if i%2!=0:
            alpha[i-1]=u*2*np.pi/3+a
            u=u+1
        else:
            alpha[i-1]=v*2*np.pi/3-a
            v=v+1

    #Calcul des angles beta
    for i in range(1,7):
        if i%2!=0:
            beta[i-1]=(u+1)*2*np.pi/3-b
            u=u+1
        else:
            beta[i-1]=v*2*np.pi/3+b
            v=v+1

    #Coordonnées de OFBi
    xf=rf*np.cos(beta)
    yf=rf*np.sin(beta)
    zf=0*np.cos(beta)
    
    #Coordonnées de OMAi dans le repère RM
    xm=rm*np.cos(alpha)
    ym=rm*np.sin(alpha)

    #Coordonnées de OMAi dans le repère RF
    xmf=(-np.sin(theta1)*np.sin(theta2)*np.sin(theta3)+np.cos(theta1)*np.cos(theta3))*xm-np.sin(theta1)*np.cos(theta2)*ym+(np.sin(theta1)*np.sin(theta2)*np.cos(theta3)+np.cos(theta1)*np.sin(theta3))*zm
    ymf=(np.cos(theta1)*np.sin(theta2)*np.sin(theta3)+np.sin(theta1)*np.cos(theta3))*xm+np.cos(theta1)*np.cos(theta2)*ym +(-np.cos(theta1)*np.sin(theta2)*np.cos(theta3)+np.sin(theta1)*np.sin(theta3))*zm
    zmf=-(np.sin(theta3)*np.cos(theta2))*xm+np.sin(theta2)*ym+(np.cos(theta3)*np.cos(theta2))*zm

    #plt.plot(xf,yf)
    #plt.plot(xmf,ymf)
    #plt.axis('equal')

    #Coordonnées de BiAi dans le repère RF
    xt=xmf+x-xf
    yt=ymf+y-yf
    zt=zmf+z+h-zf
    
    #Normes des longueurs
    return np.sqrt(xt**2+yt**2+zt**2),xf,yf,zf,xmf,ymf,zmf

# Exemple, rotation autour de z

temps=np.arange(0,5,0.01)
amplitude_z=0.2
amplitude_thetaz=np.pi/4
pulsation=5

long=[[]]

x=0
y=0
z=0
theta1=np.pi/3
theta2=0
theta3=0

for t in temps:
    theta1=amplitude_thetaz*np.sin(pulsation*t)+np.pi/3
    if t==0:
        long=[longueurs(x,y,z,theta1,theta2,theta3)[0]]
    else:
        long=np.append(long,[longueurs(x,y,z,theta1,theta2,theta3)[0]],axis=0)

fig = plt.figure(1)
plt.plot(temps,long[:,0],temps,long[:,1],temps,long[:,2],temps,long[:,3],temps,long[:,4],temps,long[:,5])

# Tracé d'une position en 3D
long_t=longueurs(0,0,0,np.pi/3,0,0) #position initiale
xf,yf,zf,xmf,ymf,zmf=long_t[1],long_t[2],long_t[3],long_t[4],long_t[5],long_t[6]+h
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(xf, yf, zf, '-b')
ax.plot(xmf, ymf, zmf, '-g')