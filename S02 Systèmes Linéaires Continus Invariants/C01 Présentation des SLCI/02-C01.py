# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti
import numpy as np

K1=53.5
tau1=0.13
Kp=0.6

K=Kp*K1/(1+Kp*K1)
print(K)
tau=tau1/(1+Kp*K1)
print(tau)

H=lti([K],[tau,1])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks_y = np.arange(0, 1.1, 0.2)
minor_ticks_y = np.arange(0, 1.1, 0.02)
major_ticks_x = np.arange(0, 0.05, 0.005)
minor_ticks_x = np.arange(0, 0.05, 0.001)


ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

plt.plot(t,y)                       #affichage
plt.grid('on')
plt.show()

