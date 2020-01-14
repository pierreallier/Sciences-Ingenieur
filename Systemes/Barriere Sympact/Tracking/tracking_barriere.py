
import numpy as np
import matplotlib.pyplot as plt

fichier=open('point_c.txt','r')
contenu=fichier.read()
lignes=contenu.split('\n')

t=[]
xC=[]
yC=[]
e=0.109
R=0.0792

ech=e/236.9
for ligne in lignes[:-2]:
    ligne=ligne.replace(',','.')
    data=ligne.split(';')
    t.append(float(data[0]))
    xC.append(ech*float(data[1]))
    yC.append(ech*float(data[2]))

xA=[0.]*len(t)
yA=[0.]*len(t)
xB=[0.]*len(t)
yB=[ech*236.9]*len(t)

t=np.array(t)
xA=np.array(xA)
yA=np.array(yA)
xB=np.array(xB)
yB=np.array(yB)
xC=np.array(xC)
yC=np.array(yC)

l=np.sqrt((xC-xA)**2+(yC-yA)**2)
lBC=np.sqrt((xC-xB)**2+(yC-yB)**2)

theta_1_star=np.arccos((xC-xA)/l)
theta_2=np.arctan((yC-yB)/(xC-xB))

mod=0
for i,t_m in enumerate(theta_2):
    if t_m<-1 and mod==0:
        mod=np.pi
    if t_m>1 and mod==np.pi:
        mod=0
    theta_2[i]+=mod




##function [dotl,omega_2] = fermeture_cinematique(theta_2,l,theta_1,omega_1)
##e=0.109;
##R=0.0792;
##theta_1_star=theta_1+pi/4;
##omega_2=(l/R)*omega_1/cos(theta_2-theta_1_star);
##dotl=-R*omega_2*sin(theta_2-theta_1_star);

theta_2_calc=theta_1_star-np.arcsin(e*np.cos(theta_1_star)/R);
l_calc=R*np.cos(theta_2)/np.cos(theta_1_star);

plt.figure('theta_2')
plt.plot(t,theta_2,t,theta_2_calc)

plt.figure('l')
plt.plot(t,l,t,l_calc)
plt.show()
