# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #pour l'affichage des courbes
from scipy.signal import lti    #pour l'utilisation de la classe lti

H=lti([2],[1,4,3])              #creation d'une instance de la classe
t,y=H.step()                    #appel de la méthode step de la classe lti

plt.plot(t,y)                       #affichage
plt.show()
