# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:41:02 2016

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

#Données géométriques et de simulation
e=0.125
# e=R*2**(1./2) Pour une arrivée tangentielle du galet dans la croix de Malte
R=0.088
dt=0.01
tf1=1
tf2=2
tf3=1

# Exercice 1

# Vitesse de rotation du bras pour un déplacement de 90° en 2s
omegab=np.pi/4
temps=np.arange(0,2,dt)

#Initialisation de la variable theta1
theta1=np.zeros(len(temps))
theta1[0]=np.pi/4

# Intégration de omegab pour avoir theta1
for i in range(1,len(temps)): 
    theta1[i]=dt*omegab+theta1[i-1]

# Résultats de la fermeture géométrique
theta2=theta1-np.arcsin(e*np.cos(theta1)/R)
l=R*np.cos(theta2)/np.cos(theta1)

# Tracé des figures
plt.figure(1)
plt.subplot(221)
plt.plot(temps, theta1*180/np.pi)
plt.title('Theta1')
plt.subplot(222)
plt.plot(temps, theta2*180/np.pi)
plt.title('Theta2')
plt.subplot(223)
plt.plot(theta1*180/np.pi, theta2*180/np.pi)
plt.title('Theta2/Theta1')

# Exercice 2:

# Vitesse de rotation du bras pour un déplacement de 90° en 2s
tf1,tf2,tf3=0.5,1,0.5
omegacmax=np.pi/3

t1=np.arange(0,tf1,dt)
omegac1=omegacmax*t1/tf1
t2=np.arange(tf1,tf1+tf2,dt)
omegac2=omegacmax*t2/t2
t3=np.arange(tf1+tf2,tf1+tf2+tf3,dt)
omegac3=omegacmax-(omegacmax/tf3)*(t3-(tf1+tf2))

temps=np.concatenate((t1,t2))
temps=np.concatenate((temps,t3))
omegac=np.concatenate((omegac1,omegac2))
omegac=np.concatenate((omegac,omegac3))

theta1=np.zeros(len(temps))
theta1[0]=np.pi/4
for i in range(1,len(temps)): 
    theta1[i]=dt*omegac[i]+theta1[i-1]

# Résultats de la fermeture géométrique (le -pi permet de forcer la simulation à tourner dans le même sens que le système)
theta2=theta1+np.arcsin(e*np.cos(theta1)/R)-np.pi
l=R*np.cos(theta2)/np.cos(theta1)

# Résultats de la fermeture cinématique
omegam=(R/e)*omegac/np.cos(theta2-theta1)
    
# Tracé des figures
plt.figure(2)
plt.subplot(221)
plt.plot(temps, theta1*180/np.pi)
plt.title('Theta1')
plt.subplot(222)
plt.plot(temps, theta2*180/np.pi)
plt.title('Theta2')
plt.subplot(223)
plt.plot(temps, l)
plt.title('l')
plt.subplot(224)
plt.plot(temps, omegam)
plt.title('omegam')

# La forme de la courbe omegam est prévisible car dans les positions de départ, la trajectoire du galet est tangentielle à la rainure.
