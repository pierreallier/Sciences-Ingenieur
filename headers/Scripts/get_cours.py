#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import subprocess
import MySQLdb
import getpass
import urllib

#pswd = getpass.getpass('Password:')
pswd = "46344634"

FNULL = open(os.devnull, 'w')

conn = MySQLdb.connect (host = 'www.costadoat.fr',
                        user = 'site_web',
                        passwd = pswd,
                        db = 'renaud')
#conn = MySQLdb.connect (host = 'localhost',
#                        user = 'root',
#                        passwd = '',
#                        db = 'renaud')
cursor = conn.cursor ()

#racine="C:/Users/Renaud/Documents/Renaud/Dorian/Prepa"
#racine="/mnt/c/Users/Renaud/Documents/Renaud/Dorian/Prepa"


def latex(id,seq,nom_seq,num,nom,tpe,ilot):
    if tpe=='C':
            chemin=("C:\Users\PROF\Documents\Renaud\SI\Cours")
        else:
            chemin=("C:\Users\PROF\Documents\Renaud\SI\TD")
	os.chdir(chemin)
    fichier="{0}-{1}{2}".format("%02d" % seq,tpe,"%02d" % num)
	os.system('rm -rf {0}.pdf'.format(fichier))
    url="github.com/Costadoat/S{1}/raw/master/{3}{4} {5}/".format(racine,"%02d" % seq,nom_seq,tpe,"%02d" % num,nom)
    fichier="{0}-{1}{2}".format("%02d" % seq,tpe,"%02d" % num)
    url = urllib.quote(url+fichier)
    instruction='wget -e https_proxy=10.175.63.254:3128 --no-check-certificate https://'+url
    print instruction
    subprocess.call(instruction, stdout=open(os.devnull, 'wb'), shell=True)

def compiler(seq,nom_seq):
    chemin = "{0}/S{1} {2}/".format(racine,"%02d" % seq,nom_seq)
    dossiers=os.listdir(chemin)
    if type==1:
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='C' ORDER BY id".format(seq))
    elif type==2: 
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='TD' ORDER BY id".format(seq))
    else:
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='C' OR type='TD' ORDER BY id".format(seq))
    rows2 = cursor.fetchall ()
    for row2 in rows2:
        id=row2[0]
        ilot=row2[7]
        nom=row2[1].decode('latin-1').encode('utf8')
        tpe=row2[4]
        num=row2[3]
        latex(id,seq,nom_seq,num,nom,tpe,ilot)				 
        
def latex_info(url,tpe,num):
    if tpe=='C':
            chemin=("C:\Users\PROF\Documents\Renaud\Info\Cours")
    elif tpe=='TD':
            chemin=("C:\Users\PROF\Documents\Renaud\Info\TD")
    else:
            chemin=("C:\Users\PROF\Documents\Renaud\Info\TP")
	os.chdir(chemin)
    fichier="I-{0}{1}".format(tpe,"%02d" % num)
	os.system('rm -rf {0}.pdf'.format(fichier))
	os.system('rm -rf {0}.py'.format(fichier))
    url = urllib.quote(url+fichier)
    for ext in ['.pdf','.py']:
        instruction='wget -e https_proxy=10.175.63.254:3128 --no-check-certificate https://'+url+ext
        print instruction
        subprocess.call(instruction, stdout=open(os.devnull, 'wb'), shell=True)
    
def compiler_info():
    racine_info ='github.com/Costadoat/Informatique/raw/master/'
    if type==1:
        cursor.execute ("SELECT * FROM cours_info WHERE type='C' ORDER BY id".format(seq))
    elif type==2: 
        cursor.execute ("SELECT * FROM cours_info WHERE type='TD' ORDER BY id".format(seq))
    elif type==3: 
        cursor.execute ("SELECT * FROM cours_info WHERE type='TP' ORDER BY id".format(seq))
    else:
        cursor.execute ("SELECT * FROM cours_info ORDER BY id".format(seq))
    rows2 = cursor.fetchall ()
    for row2 in rows2:
        id=row2[0]
        tpe=row2[4]
        num=row2[3]
        nom=row2[1].decode('latin-1').encode('utf8')
        if tpe=='C':
            chemin=("{0}Cours/{1}{2} {3}/".format(racine_info,tpe,"%02d" % num,nom))
        else:
            chemin=("{0}{1}/{1}{2} {3}/".format(racine_info,tpe,"%02d" % num,nom))
        latex_info(chemin,tpe,num)
        
seq=input('Re-compiler sequence (numero(1,..), toutes si("s"), info("i"), tout("t")) ?')
type=input('Compiler quoi (1:cours, 2:td, 3:tp, 0:tout) ?')

if isinstance(seq, int):
    cursor.execute ("SELECT * FROM sequences WHERE num={0} ORDER BY id".format(seq))
    rows = cursor.fetchall ()
    for row in rows:
        compiler(row[1],row[2].decode('latin-1').encode('utf8'))
elif seq=='s' or seq=='t':
    cursor.execute ("SELECT * FROM sequences ORDER BY id")
    rows = cursor.fetchall ()
    for row in rows:
        compiler(row[1],row[2].decode('latin-1').encode('utf8'))

if seq=='i':
    compiler_info()
