# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

auteur: Renaud Costadoat
"""

import numpy as np
import matplotlib.pyplot as plt

#Geometrie
L=0.05 #Entraxe 
r=0.02 #Rayon de l'excentrique

#Efforts
m=1 #Masse des bocaux
g=9.81 #Acceleration de pesanteur
P=m*g

t=np.linspace(0,3,1000)
theta1=np.linspace(-np.pi/2,-np.pi/2-2*np.pi,1000)
theta2=np.arccos((r/L)*np.cos(theta1))

Cm=r*P*((-np.sin(theta1)/np.tan(theta2))+np.cos(theta1))

plt.plot(t,Cm)
