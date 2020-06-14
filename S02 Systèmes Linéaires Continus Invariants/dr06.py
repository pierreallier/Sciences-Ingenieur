import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sys = signal.lti(0.03*800,[0.05,(1+0.03*800)])
t=np.linspace(0,0.014,150)
v_in=100*np.ones(len(t))
tout, y, x = signal.lsim(sys, v_in,t)

plt.plot(t,y)
plt.plot([0,0.014],[100,100])
plt.plot([0,0.014],[96,96])
plt.xticks(np.arange(0,0.015,0.002))
plt.yticks(range(0,101,20))
plt.grid('on')
plt.show()