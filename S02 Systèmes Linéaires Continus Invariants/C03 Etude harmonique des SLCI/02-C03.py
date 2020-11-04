# On importe les bibliothèques
from matplotlib.pyplot import *
from numpy import *
from pylab import *

K=2
w0=5
### La fonction de transfert ici H(j.w)=1/(1+0.01.j.w-w²)
def H(w):
    xi=1.4
    return K/(1 + (2*xi*1j*w)/w0 -w**2/w0**2)

### La fonction de transfert ici H(j.w)=1/(1+0.01.j.w-w²)
##def H2(w):
##    xi=0.01
##    return K/(1 + (2*xi*1j*w)/w0 -w**2/w0**2)

### La fonction de transfert ici H(j.w)=1/(1+0.01.j.w-w²)
##def H3(w):
##    xi=0.7
##    return K/(1 + (2*xi*1j*w)/w0 -w**2/w0**2)



K=1.5
tau=4
##def H(w):
##    return K/(1 + tau*1j*w)
##
##def asympt(wlist):
##    out=[]
##    for w in wlist:
##        if w<1/tau:
##            out.append(K)
##        else:
##            out.append(K/(tau*1j*w))
##    return out

##tau1,tau2=0.4,15
##def H(w):
##    return K/((1 + tau1*1j*w)*(1 + tau2*1j*w))

##def asympt(wlist):
##    out=[]
##    for w in wlist:
##        if w<1/tau2:
##            out.append(K)
##        elif w>=1/tau2 and w<1/tau1:
##            out.append(K/(tau2*1j*w))
##        else:
##            out.append(K/(tau1*1j*w*tau2*1j*w))
##    return out


##def H(w):
##    return K/w

##K=2
##def H(w):
##    return K*w/w

def trace(zoom,ordre,H):
    # Découpage régulier des puissances en base 10 de la pulsation ici de 10^-2 à 10^3
    if ordre==1:
        fig=figure('Diagrammes Bode')
        w0=1/tau
        puissance_w=arange(log10(w0)-4,log10(w0)+3,0.01)
    else:
        w0=100
        if zoom==False:
            fig=figure('Diagrammes Bode')
            puissance_w=arange(log10(w0)-3,log10(w0)+3,0.01)
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
    axes = gca()
    axes.set_xlim(0.005,200)
    axes.set_ylabel('Gain (dB)')
    grid(True) # Activation de la grille
    subplot(212)
    semilogx(W,phase) #Tracé en semilog du module
    axes = gca()
    axes.set_ylabel('Phase (deg)')
    axes.set_xlabel('Pulsation $(rad.s^{-1})$')
    axes.set_xlim(0.005,200)
    grid(True) #Activation de la grille
    #On montre le graphique

ordre=1

if ordre==1:
    trace(False,1,H)
#    trace(False,1,asympt)
else:
    trace(False,2,H)    
    if xi<0.7:
        trace(True,2,H)
    
show()
