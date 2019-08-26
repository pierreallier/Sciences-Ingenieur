# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:41:02 2016
@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

#Données géométriques et de simulation
a=0.08
b=0.065
l1=0.08
l2=0.27

p=0.004
l0=0.056
dt=0.01

#Masses
m=1*1.0
P=9.81*m

print 'Exercice 1:'

# Vitesse de rotation du bras pour un déplacement de 90° en 1s
omegab=np.pi/2
temps=np.arange(0,1,dt)

#Initialisation de la variable theta1
theta1=np.zeros(len(temps))
theta1[0]=0

# Intégration de omegab pour avoir theta1
for i in range(1,len(temps)): 
    theta1[i]=dt*omegab+theta1[i-1]

# Résultats de la fermeture géométrique
theta3=(l1*np.sin(theta1)-a)/(b+l1*np.cos(theta1))

# Correction pour avoir la dérivée de theta 2 continue


# Tracé des figures
plt.figure(1)
plt.subplot(221)
plt.plot(temps, theta1)
plt.title('Theta1')
plt.subplot(222)
plt.plot(temps, thetam)
plt.title('Thetam')
plt.subplot(223)
plt.plot(temps, theta3)
plt.title('theta3')


Cm=(p/(2*np.pi))*(l2*np.cos(theta1)*P)/(np.cos(theta3)*l1*(np.cos(theta1)*np.tan(theta3)-np.sin(theta1)))
plt.figure(2)
plt.plot(theta1,Cm)