# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *

K=1
xi=0.2
w0=100
# La fonction de transfert ici H(j.w)=1/(1+0.01.j.w-w²)
def H(w):
    return K/(1 + (2*xi*1j*w)/w0 -w**2/w0**2)

K=20
tau=4
def H(w):
    return K/((1 + tau*1j*w)*1j*w)

def trace(zoom,ordre):
    # Découpage régulier des puissances en base 10 de la pulsation ici de 10^-2 à 10^3
    if ordre==1:
        fig=figure('Diagrammes Bode')
        w0=1/tau
        puissance_w=arange(log10(w0)-2,log10(w0)+2,0.01)
    else:
        w0=100
        if zoom==False:
            fig=figure('Diagrammes Bode')
            puissance_w=arange(log10(w0)-2,log10(w0)+2,0.01)
        else:
            fig=figure('Zoom Diagrammes Bode')
            puissance_w=arange(log10(w0)-0.1,log10(w0)+0.1,0.01)
    # Les pulsations w
    W=10**puissance_w
    # La phase en degré
    phase = angle(H(W),'deg')
    # Le module en dB
    module = 20*log10(absolute(H(W)))
    #Tracer du diagramme de Bode
    subplot(211) # Permet d’afficher plusieurs graphes (nombre de graphe (2), colonne (1), ligne (1))
    semilogx(W,module) # Tracé en semilog du module
    grid(True) # Activation de la grille
    subplot(212)
    semilogx(W,phase) #Tracé en semilog du module
    grid(True) #Activation de la grille
    #On montre le graphique

ordre=1

if ordre==1:
    trace(False,1)
else:
    trace(False,2)    
    if xi<0.7:
        trace(True,2)
    
show()
