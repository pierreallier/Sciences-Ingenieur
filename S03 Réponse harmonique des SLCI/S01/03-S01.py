# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:59:06 2019

@author: Renaud
"""


import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,2,0.01)
K=10
E0=2
tau=0.25
def premier_ordre(t):
    return E0*K*(1-np.exp(-t/tau))

plt.figure(1)
plt.plot(t,premier_ordre(t))
plt.plot(t,np.ones(len(t))*premier_ordre(t[-1]),"k--")
plt.plot(t,0.95*np.ones(len(t))*premier_ordre(t[-1]),"r")
plt.plot([0,tau],[0,E0*K],'g')
plt.plot([tau,tau],[E0*K,0],'g--')
plt.plot([3*tau,3*tau],[0,0.95*E0*K],"r--")
plt.axis([0, 2,0,22])
plt.grid(True)
plt.xlabel("temps (s)")
plt.ylabel("sortie")
plt.savefig("Premier_ordre_temp.pdf")


tau1=0.15
tau2=0.4
def second_ordre_xi_sup(t):
    return E0*K*(1-np.exp(-t/tau1))*(1-np.exp(-t/tau2))

plt.figure(2)
plt.plot(t,second_ordre_xi_sup(t))
plt.plot(t,np.ones(len(t))*second_ordre_xi_sup(t[-1]),"k--")
plt.plot(t,0.95*np.ones(len(t))*second_ordre_xi_sup(t[-1]),"r")
plt.plot([3*tau,3*tau],[0,0.95*E0*K],"r--")
plt.axis([0, 2,0,22])
plt.grid(True)
plt.xlabel("temps (s)")
plt.ylabel("sortie")
plt.savefig("Second_ordre_xi_sup_temp.pdf")

xi=0.6
omega0=8
phi=10
def second_ordre_xi_inf(t):
    return 10*(1-np.exp(-xi*omega0*t)/np.sqrt(1-xi**2)*np.sin(omega0*t+phi))

plt.figure(3)
plt.plot(t,second_ordre_xi_inf(t))
plt.savefig("Second_ordre_xi_inf_temp.pdf")

def H(w):
    return 1/(1 + 0.01*1j*w -w*w)

puissance_w=np.arange(-2,3,0.01)
W=10**puissance_w

phase = np.angle(H(W),'deg')
module = 20*np.log(np.absolute(H(W)))

plt.subplot(211)
plt.semilogx(W,module)
plt.grid(True)
plt.subplot(212)
plt.semilogx(W,phase)

plt.grid(True)
