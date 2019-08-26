# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

auteur: Renaud Costadoat
"""

import numpy as np
import matplotlib.pyplot as plt

#Geometrie
L=0.125 #Entraxe 
r=0.088 #Rayon de l'indexeur
e=0.18 #Rayon d'appui des bocaux
alpha=np.pi/4

#Efforts
f=0.03 #Coefficient de frottement
m=0.1 #Masse des bocaux
g=9.81 #Acceleration de pesanteur
F=m*g*f

t=np.linspace(0,1,1000)
theta2=np.linspace(-np.pi/4,-3*np.pi/4,1000)
theta1=np.arctan((L+r*np.sin(theta2))/(r*np.cos(theta2)))-alpha

for i in range(len(theta1)):
    if theta1[i]<0:
        theta1[i]+=np.pi

l=r*np.cos(theta2)/np.cos(theta1+alpha)

beta=theta2-(theta1+alpha)

Cm=-e*(F+F)*r*np.cos(beta)/(l)

plt.plot(theta2,Cm)

