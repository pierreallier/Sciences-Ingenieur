#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import subprocess
import sys
import os
import os.path
import codecs

 
conn = MySQLdb.connect (host = 'www.costadoat.fr',
                        user = 'site_web',
                        passwd = '46344634',
                        db = 'renaud')
#conn = MySQLdb.connect (host = 'localhost',
#                        user = 'root',
#                        passwd = '',
#                        db = 'renaud')
cursor = conn.cursor ()

racine="/mnt/c/Users/Renaud/Documents/Renaud/Dorian/Prepa"

def gen_intro(n):
    cursor.execute ("SELECT C.Id, C.Nom, C.Sequence, C.Num, C.Type, C.Ilot, S.Nom, C.Description FROM cours C JOIN sequences S ON C.Sequence=S.Id WHERE Sequence={0}".format(n))
    rows = cursor.fetchall ()

    for row in rows:
            cursor2 = conn.cursor ()
            cursor2.execute ("SELECT * FROM competence_util WHERE Id_cours={0}".format(row[0]))
            rows2 = cursor2.fetchall ()
            competences =''
            nb_comp = 0
            for row2 in rows2:
                    cursor3 = conn.cursor ()
                    cursor3.execute ("SELECT * FROM competences WHERE Id={0}".format(row2[2]))
                    rows3 = cursor3.fetchall ()
                    comp =''
                    for row3 in rows3:
                            comp = row3[1] + ': ' + row3[2] 
                            cursor3.close ()
                    cursor2.close ()
                    competences = competences + comp + ' \\\\ &  '
                    nb_comp += 1
            cursor4 = conn.cursor ()
            cursor4.execute ("SELECT Id_systeme FROM systeme_util WHERE Id_cours={0}".format(row[0]))
            rows4 = cursor4.fetchall ()
            systemes = ''
            img = ''
            i=-1
            numero_image = ['imageun','imagedeux','imagetrois','imagequatre','imagecinq','imagesix']
            for row4 in rows4:
                    i += 1
                    cursor5 = conn.cursor ()
                    cursor5.execute ("SELECT * FROM systemes WHERE Id={0}".format(row4[0]))
                    rows5 = cursor5.fetchall ()
                    sys =''
                    for row5 in rows5:
                        sys = row5[1].decode('latin-1').encode('utf8')
                        img = img + "\\newcommand{{\{0}}}{{{1}}}\r".format(numero_image[i],"%05d" % row5[0])
                        cursor5.close ()
                    cursor4.close ()
                    systemes = systemes + sys + ', '
            competences = competences[:-7]
            systemes = systemes[:-2]
            nom=row[1].decode('latin-1').encode('utf8')
            nom_seq=row[6].decode('latin-1').encode('utf8')
            if row[5] == 0:
                chemin = "{0}/S{1} {2}/{3}{4} {5}/intro.tex".format(racine,"%02d" % row[2],nom_seq,row[4],"%02d" % row[3],nom)
                chemin_qr = "{0}/S{1} {2}/{3}{4} {5}/img".format(racine,"%02d" % row[2],nom_seq,row[4],"%02d" % row[3],nom)
                if not os.path.isdir(chemin_qr):
                    os.mkdir(chemin_qr)
            else:
                chemin = "{0}/S{1} {2}/{3}{4} {5}/Ilot_{6} {7}/intro.tex".format(racine,"%02d" % row[2],nom_seq,row[4],"%02d" % row[3],nom,"%02d" % row[5],sys)
                chemin_qr = "{0}/S{1} {2}/{3}{4} {5}/Ilot_{6} {7}/img".format(racine,"%02d" % row[2],nom_seq,row[4],"%02d" % row[3],nom,"%02d" % row[5],sys)
                if not os.path.isdir(chemin_qr):
                    os.mkdir(chemin_qr)
            if qrgen==1:
                if row[5] == 0:
                    web="https://github.com/Costadoat/S{0}/blob/master/{1}{2} {3}/{0}-{1}{2}.pdf?raw=true".format("%02d" % row[2],row[4],"%02d" % row[3],nom,"%02d" % row[5]).replace(" ","%20")                    
                else:
                    web="https://github.com/Costadoat/S{0}/blob/master/{1}{2} {3}/Ilot_{4} {5}/{0}-{1}{2}-I{3}.pdf?raw=true".format("%02d" % row[2],row[4],"%02d" % row[3],nom,"%02d" % row[5],sys).replace(" ","%20")
                os.chdir("{0}/headers/Scripts".format(racine))
                os.system("python ressources/generate.py ressources/LogoRen.svg {0} '{1}'/qrcode.svg".format(web,chemin_qr))
                os.chdir(chemin_qr)
                #os.execl("C:\Program Files\Inkscape\inkscape.exe", "-z", "-f {0}/qrcode.svg".format(chemin_qr), "-w 400", "-j", "-e {0}/qrcode.png".format(chemin_qr))
                os.system("inkscape -z -f qrcode.svg -w 400 -j -e qrcode.png".format(chemin_qr))
            fichier = open(chemin, "w")
            info = "\\newcommand{{\\id}}{{{0}}}\r\\newcommand{{\\nom}}{{{1}}}\r\\newcommand{{\\sequence}}{{{2}}}\r\\newcommand{{\\num}}{{{3}}}\r\\newcommand{{\\type}}{{{4}}}\r\\newcommand{{\\descrip}}{{{5}}}\r\\newcommand{{\\competences}}{{{6}}}\r\\newcommand{{\\nbcomp}}{{{7}}}\r\\newcommand{{\\systemes}}{{{8}}}\r\\newcommand{{\\ilot}}{{{9}}}\r{10}".format(row[0],row[1],"%02d" % row[2],"%02d" % row[3],row[4],row[7],competences,nb_comp,systemes.decode('utf8').encode('latin-1'),row[5],img)
            #print("%s" % (info))
            if row[4]=='TP':
                fichier.write(info.decode('latin-1').encode('utf8'))
            else:
                fichier.write(info.decode('latin-1').encode('utf8'))            
            fichier.close()

n=input('Mise a jour de la sequence (all=2000) ')
qrgen=raw_input('Generer les QRCode ? (o/N) ')
if qrgen=='o':
    qrgen=1
else:
    qrgen=0
    
if n==2000:
    for sequence in range(15):
        print sequence
        gen_intro(sequence)
else:
    gen_intro(n)

cursor.close () 
conn.close ()