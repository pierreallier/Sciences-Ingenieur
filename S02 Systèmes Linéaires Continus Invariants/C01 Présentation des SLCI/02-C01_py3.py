import control
import matplotlib.pyplot as plt
import numpy as np

###### Ne pas modifier les fonctions suivantes ###############

def constructions_ordre_1(E,G,tau):
    plt.plot([0,t_out[-1]],[0.95*G*E,0.95*G*E])
    plt.plot([3*tau,3*tau],[0,G*E],'r--')
    plt.plot([tau,tau],[0,G*E],'g--')
    plt.plot([0,tau],[0,G*E],'g--')

def constructions_ordre_2(E,G,xsi,omega0):
    if xsi>0.7:
        plt.plot([0,t_final],[0.95*G*E,0.95*G*E])
    else:
        D=G*np.exp(-np.pi*xsi/np.sqrt(1-xsi**2))
        th=np.pi/(omega0*np.sqrt(1-xsi**2))
        T=2*th
        plt.plot([0,t_final],[0.95*G*E,0.95*G*E],'orange')
        plt.plot([0,t_final],[1.05*G*E,1.05*G*E],'orange')
        plt.plot([0,t_final],[D+G*E,D+G*E])
        plt.plot([th,th],[0,D+G*E],'g--')
        plt.plot([th+T,th+T],[0,D+G*E],'g--')
    
###### Définir la fonction temporelle s(t) #######################
def ordre1(t):
    return G*E*(1-np.exp(-t/tau))

def ordre2_xsi_plus_grand_1(t):
    tau1=1/(omega0*(xsi+np.sqrt(xsi**2-1)))
    tau2=1/(omega0*(xsi-np.sqrt(xsi**2-1)))    
    return G*E*(1-tau1/(tau1-tau2)*np.exp(-t/tau1)+tau2/(tau1-tau2)*np.exp(-t/tau2))

def ordre2_xsi_plus_petit_1(t):
    xsi1=xsi/np.sqrt(1-xsi**2)
    omega1=omega0*np.sqrt(1-xsi**2)
    gain1=np.exp(-omega0*xsi*t)/(np.sqrt(1-xsi**2))
    return G*E*(1-gain1*np.cos(omega1*t-np.arctan(xsi1)))

###### Tracé des courbes temporelles #############################
t_final=10     # t_final (durée du tracé à modifier si besoin)
t=np.linspace(0,t_final,1000)

E=2             # Valeur de l'échelon d'entrée

## Fonction du premier ordre
G=10            # Gain de la fonction de transfert
tau=1           # Constante de temps tau
sys = control.TransferFunction(G*E, [tau,1])

## Fonction du second ordre
G=10            # Gain de la fonction de transfert
xsi=0.3         # Coefficient d'amortissemrnt xsi
omega0=100      # Pulsation propre omega0
#sys = control.TransferFunction(G*E, [1/omega0**2,2*xsi/omega0,1])

# Tracé temporel issu de la fonction de transfert
t_out,s_l=control.step_response(sys,t,0)
plt.plot(t_out,s_l)

# Tracé de la fonction temporelle s(t)
plt.plot(t,ordre1(t))

###### Construction des valeurs remarquables des réponses #######
#constructions_ordre_1(E,G,tau)
#constructions_ordre_2(E,G,xsi,omega0)

plt.show()
