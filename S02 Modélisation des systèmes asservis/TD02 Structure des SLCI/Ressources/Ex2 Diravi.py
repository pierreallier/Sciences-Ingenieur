# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 17:31:43 2016

@author: costa
"""

import math

Ka=34./57.
Kb=0.4
Kc=1/50.*360*10**3
Kd=Ka
k=0.24*10**3
S=3000
M=500
f=60*10**(-3)/60
V=10**(-3)*10**(-3)



K=Ka/(Kc*Kd)
print 'K=%s' % format(K)

A=S/(Kb*k*Kc*Kd)
print 'A=%s' % format(A)

B=M*f/(S*Kb*k*Kc*Kd)
print 'B=%s' % format(B)

C=M*V/(S*Kb*k*Kc*Kd)
print 'C=%s' % format(C)

w0=math.sqrt(1/B)
print 'W0=%s' % format(w0)

xi=w0*A/2.
print 'xi=%s' % format(xi)

