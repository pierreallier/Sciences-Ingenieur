#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import subprocess
import sys
import os
import os.path


 
conn = MySQLdb.connect (host = 'www.costadoat.fr',
                        user = 'site_web',
                        passwd = '46344634',
                        db = 'renaud')
#conn = MySQLdb.connect (host = 'localhost',
#                        user = 'root',
#                        passwd = '',
#                        db = 'renaud')
cursor = conn.cursor ()

racine="/mnt/c/users/costa/Documents/Renaud/Dorian/Prepa"

def gen_intro(n):
    cursor.execute ("SELECT sequences.num, sequences.nom, cours.type, cours.num, cours.nom, cours.ilot, systemes.Systeme FROM cours JOIN sequences ON sequences.Id=cours.sequence LEFT JOIN systeme_util ON systeme_util.Id_cours=cours.Id LEFT JOIN systemes on systemes.Id=systeme_util.Id_systeme WHERE Sequence={0} GROUP BY cours.Id order by cours.sequence, cours.type, cours.num, cours.ilot".format(n))
    rows = cursor.fetchall ()

    for row in rows:
        if row[5] == 0:
            chemin_old = "{0}/S{1} {2}/{3}{4}/".format(racine,"%02d" % row[0],row[1],row[2],"%02d" % row[3]).decode('latin1')
            chemin_new = "{0}/S{1} {2}/{3}{4} {5}/".format(racine,"%02d" % row[0],row[1],row[2],"%02d" % row[3],row[4]).decode('latin1')
            #com1=['mv',chemin_old,chemin_new]
            #subprocess.call(com1, stdout=open(os.devnull, 'wb'))
        else:
            chemin_old = "{0}/S{1} {2}/{3}{4} {5}/Ilot_{6}".format(racine,"%02d" % row[0],row[1],row[2],"%02d" % row[3],row[4],"%02d" % row[5]).decode('latin1')
            chemin_new = "{0}/S{1} {2}/{3}{4} {5}/Ilot_{6} {7}".format(racine,"%02d" % row[0],row[1],row[2],"%02d" % row[3],row[4],"%02d" % row[5],row[6]).decode('latin1')
            com1=['mv',chemin_old,chemin_new]
            subprocess.call(com1, stdout=open(os.devnull, 'wb'))        


for sequence in range(15):
    print sequence
    gen_intro(sequence)

cursor.close () 
conn.close ()