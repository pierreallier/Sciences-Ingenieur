# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

import matplotlib.pyplot as plt
import numpy as np

b=3346.6
m=50.
k=14000.
E0=100.
p1=(-b+np.sqrt(b**2-4*m*k))/(2*m)
p2=(-b-np.sqrt(b**2-4*m*k))/(2*m)
A=p2*E0/(k*p1*(p2-p1))
B=-p1*E0/(k*p2*(p2-p1))
C=E0/k

t = np.linspace(0, 2, 100)
s = -A*p1*np.exp(p1*t)-B*p2*np.exp(p2*t)+C
plt.plot(t, s)
