import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sys = signal.lti(0.5,[0.05,1])
t=np.linspace(0,0.35,150)
v_in=220*np.ones(len(t))
tout, y, x = signal.lsim(sys, v_in,t)

plt.plot(t,y)
plt.plot([0,0.05],[0,0.5*220])
plt.plot([0,0,0.35],[0,0.5*220,0.5*220])
plt.plot([0,0.35],[0.95*0.5*220,0.95*0.5*220])
plt.plot([0.15,0.15],[0,0.95*0.5*220])
plt.xticks(np.arange(0,0.36,0.05))
plt.yticks(range(0,161,20))
plt.grid('on')
plt.show()