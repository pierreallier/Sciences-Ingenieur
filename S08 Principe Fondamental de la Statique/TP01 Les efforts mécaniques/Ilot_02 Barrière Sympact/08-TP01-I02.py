# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:41:02 2016
@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

#Données géométriques et de simulation
e=0.112
l2=0.081
lp=1
alpha=np.pi/4

dt=0.01

#Masses
m=1*1.0
P=9.81*m

t=np.linspace(0,3,1000)
theta1=np.linspace(0,np.pi/2,1000)
theta2=theta1+alpha-np.arcsin((e/l2)*np.cos(theta1+alpha))
l=l2*np.cos(theta2)/np.cos(theta1+alpha)
Cm=(l2*lp*P*np.cos(theta1)/l)*np.cos((theta1+alpha)-theta2)


plt.plot(np.pi/2-theta1,Cm)
