#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import subprocess
import MySQLdb

FNULL = open(os.devnull, 'w')

conn = MySQLdb.connect (host = 'www.costadoat.fr',
                        user = 'site_web',
                        passwd = '46344634',
                        db = 'renaud')
#conn = MySQLdb.connect (host = 'localhost',
#                        user = 'root',
#                        passwd = '',
#                        db = 'renaud')
cursor = conn.cursor ()

racine="C:/Users/Renaud/Documents/Renaud/Dorian/Prepa"
racine="/mnt/c/Users/Renaud/Documents/Renaud/Dorian/Prepa"

def latex(id,seq,nom_seq,num,nom,tpe,ilot):
    if ilot != 0:
        cursor.execute ("SELECT Systeme FROM systemes S JOIN systeme_util SU ON S.Id=SU.Id_systeme WHERE SU.Id_cours={0}".format(id))
        rowss = cursor.fetchall ()
        systeme=rowss[0][0].decode('latin-1').encode('utf8')
        path="{0}/S{1} {2}/{3}{4} {5}/Ilot_{6} {7}".format(racine,"%02d" % seq,nom_seq,tpe,"%02d" % num,nom,"%02d" % ilot,systeme)
        fichier="{0}-{1}{2}-I{3}".format("%02d" % seq,tpe,"%02d" % num,"%02d" % ilot)
    else:
        path="{0}/S{1} {2}/{3}{4} {5}".format(racine,"%02d" % seq,nom_seq,tpe,"%02d" % num,nom)
        fichier="{0}-{1}{2}".format("%02d" % seq,tpe,"%02d" % num)
    os.chdir(path)
    com1=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-jobname={0}'.format(fichier), '\def\public{}', '\input{{{0}.tex}}'.format(fichier)]
    com2=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-jobname={0}_prive'.format(fichier), '\def\prive{}', '\input{{{0}.tex}}'.format(fichier)]
    if os.path.isfile('{0}/{1}.tex'.format(path,fichier)):
        subprocess.call(com1, stdout=FNULL, stderr=subprocess.STDOUT)
        subprocess.call(com1, stdout=FNULL, stderr=subprocess.STDOUT)
        subprocess.call(com2, stdout=FNULL, stderr=subprocess.STDOUT)
        subprocess.call(com2, stdout=FNULL, stderr=subprocess.STDOUT)
        print '{0} Ok!'.format(fichier)
    else: 
		print 'Pas de fichier {0}/{1}.tex'.format(path,fichier)
		print '{0} Ko :('.format(fichier)    

def compiler(seq,nom_seq):
    chemin = "{0}/S{1} {2}/".format(racine,"%02d" % seq,nom_seq)
    dossiers=os.listdir(chemin)
    if type==1:
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='C' ORDER BY id".format(seq))
    elif type==2: 
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='TD' ORDER BY id".format(seq))
    elif type==3: 
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='TP' ORDER BY id".format(seq))
    elif type==4: 
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} AND type='KH' ORDER BY id".format(seq))
    else:
        cursor.execute ("SELECT * FROM cours WHERE sequence={0} ORDER BY id".format(seq))
    rows2 = cursor.fetchall ()
    for row2 in rows2:
        id=row2[0]
        ilot=row2[7]
        nom=row2[1].decode('latin-1').encode('utf8')
        tpe=row2[4]
        num=row2[3]
        latex(id,seq,nom_seq,num,nom,tpe,ilot)				 
        
def latex_info(path,tpe,num):
    fichier="I-{0}{1}".format(tpe,"%02d" % num)
    os.chdir(path)
    print path
    if tpe=='TP':
        com1=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-shell-escape', '-jobname={0}'.format(fichier), '\def\public{}', '\input{{{0}.tex}}'.format(fichier), ' > /dev/null']
        com2=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-shell-escape', '-jobname={0}_prive'.format(fichier), '\def\prive{}', '\input{{{0}.tex}}'.format(fichier), ' > /dev/null']
    else:
        com1=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-jobname={0}'.format(fichier), '\def\public{}', '\input{{{0}.tex}}'.format(fichier), ' > /dev/null']
        com2=['pdflatex', '-synctex=1', '-interaction=nonstopmode', '-jobname={0}_prive'.format(fichier), '\def\prive{}', '\input{{{0}.tex}}'.format(fichier), ' > /dev/null']
    if os.path.isfile('{0}/{1}.tex'.format(path,fichier)):
        proc = subprocess.call(com1, stdout=FNULL, stderr=subprocess.STDOUT)
        proc = subprocess.call(com1, stdout=FNULL, stderr=subprocess.STDOUT)
        proc = subprocess.call(com2, stdout=FNULL, stderr=subprocess.STDOUT)
        proc = subprocess.call(com2, stdout=FNULL, stderr=subprocess.STDOUT)
        print '{0} Ok!'.format(fichier)
    else: 
		print 'Pas de fichier {1}.tex'.format(path,fichier)
		print '{0} Ko :('.format(fichier)
    
def compiler_info():
    racine_info ='{0}/Informatique/'.format(racine)
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
            chemin=("{0}Cours/{1}{2} {3}".format(racine_info,tpe,"%02d" % num,nom))
        else:
            chemin=("{0}{1}/{1}{2} {3}".format(racine_info,tpe,"%02d" % num,nom))
        latex_info(chemin,tpe,num)
        
seq=input('Re-compiler sequence (numero(1,..), toutes si("s"), info("i"), tout("t")) ?')
type=input('Compiler quoi (1:cours, 2:td, 3:tp, 4:kh, 0:tout) ?')

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
