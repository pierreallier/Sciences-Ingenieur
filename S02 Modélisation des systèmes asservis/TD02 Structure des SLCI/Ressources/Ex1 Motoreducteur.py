# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 17:31:43 2016

@author: costa
"""

KE=0.6
KM=0.7
R=4.5
JT=2.8
fT=1.5*10**(-3)
K=200
Kv=0.01*3.14/30
T=15*10**(-3)
ro=0.7

K1=KM/(R*fT+KE*KM)
print K1

T1=R*JT/(R*fT+KE*KM)
print T1

evs=1/(1+K*K1*Kv)
print evs

KFTBF=ro*K*K1/(1+K*K1*Kv)
print KFTBF

