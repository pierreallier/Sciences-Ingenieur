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
l1=0.1
p=0.004
l0=0.056
dt=0.01

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
l=np.sqrt((b+l1*np.cos(theta1))**2+(l1*np.sin(theta1)-a)**2)
thetam=(l-l0)*2*np.pi/p
theta3=np.arccos((b+l1*np.cos(theta1))/l)

# Correction pour avoir la dérivée de theta 2 continue
s=0
for i in range(1,len(temps)): 
    if (1-(b+l1*np.cos(theta1[i]))/l[i]<10**(-6) or s==1):
        s=1
        theta3[i]=-theta3[i]

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

print 'Exercice 2:'

# Définition du trapèze de vitesse pour un déplacement total de pi/2
tf1,tf2,tf3=0.25,0.5,0.25
omegabmax=np.pi/1.5

t1=np.arange(0,tf1,dt)
omegab1=omegabmax*t1/tf1
t2=np.arange(tf1,tf1+tf2,dt)
omegab2=omegabmax*t2/t2
t3=np.arange(tf1+tf2,tf1+tf2+tf3,dt)
omegab3=omegabmax-(omegabmax/tf3)*(t3-(tf1+tf2))

temps=np.concatenate((t1,t2))
temps=np.concatenate((temps,t3))
omegab=np.concatenate((omegab1,omegab2))
omegab=np.concatenate((omegab,omegab3))

#Initialisation de la variable theta1
theta1=np.zeros(len(temps))
theta1[0]=0

# Intégration de omegab pour avoir theta1
for i in range(1,len(temps)): 
    theta1[i]=dt*omegab[i]+theta1[i-1]

# Résultats de la fermeture géométrique
l=np.sqrt((b+l1*np.cos(theta1))**2+(l1*np.sin(theta1)-a)**2)
thetam=(l-l0)*2*np.pi/p
theta3=np.arccos((b+l1*np.cos(theta1))/l)

# Correction pour avoir la dérivée de theta 2 continue
s=0
theta3=-theta3
for i in range(1,len(temps)): 
    if (1-(b+l1*np.cos(theta1[i]))/l[i]<10**(-5) or s==1):
        s=1
        theta3[i]=-theta3[i]
        
# Résultats de la fermeture cinématique
omegam=(2*np.pi/p)*(-np.sin(theta1-theta3)*l1)*omegab

# Calcul de omegam en dérivant thetam pour vérifier le résultat des calculs cinématiques
omegam2=np.zeros(len(temps))
for i in range(1,len(temps)): 
    omegam2[i]=(thetam[i]-thetam[i-1])/dt


# Tracé des figures
plt.figure(2)
plt.subplot(221)
plt.plot(temps, omegab)
plt.title('Omegab')
plt.subplot(222)
plt.plot(temps, theta1*180/np.pi)
plt.title('Theta1')
plt.subplot(223)
plt.plot(temps, omegam,temps, omegam2)
plt.title('Omegam')
plt.subplot(224)
plt.plot(temps, thetam)
plt.title('Thetam')


# Lire le fichier du Logiciel Maxpid (expérimental)
data=[]
mon_fichier = open("results.txt", "r")
contenu = mon_fichier.read()
ligne=contenu.split('\n')
for i in range(len(ligne)-1):
    data.append(ligne[i].split('     ')[1:8])
mon_fichier.close()

temps_exp=np.zeros(len(data))
cons_exp=np.zeros(len(data))
theta1_exp=np.zeros(len(data))
omegab_exp=np.zeros(len(data))
omegam_exp=np.zeros(len(data))
for i in range(len(data)):
    temps_exp[i]=data[i][0]
    cons_exp[i]=data[i][1]
    theta1_exp[i]=data[i][2]
    omegab_exp[i]=data[i][5]
    omegam_exp[i]=data[i][6]

thetam_exp=np.zeros(len(temps_exp))
thetam_exp[0]=0
for i in range(1,len(omegam_exp)):
    thetam_exp[i]=thetam_exp[i-1]+dt*omegam_exp[i]

    
# Tracé des figures
plt.figure(3)
plt.subplot(221)
plt.plot(temps_exp/1000, omegab_exp)
plt.title('Omegab')
plt.subplot(222)
plt.plot(temps_exp/1000, cons_exp, temps_exp/1000, theta1_exp)
plt.title('Theta1 (consigne/mesure)')
plt.subplot(223)
plt.plot(temps_exp/1000, -omegam_exp)
plt.title('Omegam')
plt.subplot(224)
plt.plot(temps_exp/1000, 200-thetam_exp)
plt.title('Thetam')