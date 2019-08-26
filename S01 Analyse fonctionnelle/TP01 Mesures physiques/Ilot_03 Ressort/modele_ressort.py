    # -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 17:41:02 2016

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

T=input('Duree de la mesure (en s) ?')

k=input('Raideur du ressort (en N/m) ?')
m=input('Masse suspendue (en kg) ?')
w0=np.sqrt(k/m)
xsi_max=np.sqrt(k*m)
L=input('Coefficient d amortissement (N/(m/s)) (<'+str(xsi_max)+') ?')
xsi=L/(2*np.sqrt(k*m))
print xsi
K0=m*9.81/k
t=np.linspace(0,T,1000)

s=K0*(1.-(w0/np.sqrt(1.-xsi**2.))*np.exp(-xsi*w0*t)*np.sin(w0*t*np.sqrt(1-xsi**2.)))
print s
plt.plot(t,s)