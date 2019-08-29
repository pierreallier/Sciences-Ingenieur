#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import subprocess

FNULL = open(os.devnull, 'w')
 
lycee=input('Quel proxy utiliser ? (0=aucun, 1=dorian, 2=chaptal) ?')

if lycee==0:
	com='cp -rf /mnt/c/Users/Renaud/.gitconfig_normal /mnt/c/Users/Renaud/.gitconfig'
	print 'Aucun proxy'
elif lycee==1:
	com='cp -rf /mnt/c/Users/Renaud/.gitconfig_dorian /mnt/c/Users/Renaud/.gitconfig'
	print 'Proxy Dorian'
else:
	com='cp -rf /mnt/c/Users/Renaud/.gitconfig_chaptal /mnt/c/Users/Renaud/.gitconfig'
	#com0='git config --global http.proxy http://192.168.1.1:3128 #chaptal2
	print 'Proxy Chaptal'

#subprocess.call(com, stdout=open(os.devnull, 'wb'))
subprocess.call(com, shell=True)