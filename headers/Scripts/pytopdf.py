# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:11:46 2016

@author: Renaud
"""


def contenu(latex):
    header = r'''\documentclass[a4paper,12pt,titlepage,twoside]{article}
    \usepackage[T1]{fontenc}
    \usepackage[french]{babel}
    \usepackage[gen]{eurosym}
    \usepackage{verbatim}
    \usepackage{textcomp}
    \setlength{\hoffset}{-18pt} \setlength{\oddsidemargin}{0pt}
    \setlength{\evensidemargin}{0pt}
    \setlength{\marginparwidth}{00pt}
    \setlength{\textwidth}{481pt}
    \setlength{\voffset}{-18pt}
    \setlength{\marginparsep}{7pt}
    \setlength{\topmargin}{-30pt}
    \setlength{\headheight}{5pt}
    \setlength{\headsep}{20pt}
    \setlength{\footskip}{30pt}
    \setlength{\textheight}{700pt}

    \begin{document}

    \begin{center}
    Rapport des TIPE
    \end{center}

    '''

    main  = r''' '''
    fichier=open('formulaire_tipe_ptsi_dorian.csv')
    contenu=fichier.read()
    fichier.close()
    lignes=contenu.split("123456\n")
    if latex==1:
        for ligne in lignes[3:-1]:
            main+=r'''\newpage'''+'\n'
            data=ligne.split(";")
            print(data[0])
            main+=r'''\textbf{'''+str(data[0])+r''' '''+str(data[1])+r'''}'''+'\n \n'
            main+=r'''\begin{center}'''+str(data[2])+r'''\end{center}'''+'\n \n'
            main+=r'''\textbf{Résumé en anglais:}'''+str(data[3])+'\n \n'
            main+=r'''\textbf{Bibliographie commentée:}'''+str(data[4])+'\n \n'
            main+=r'''\textbf{Références bibliographiques:} \begin{verbatim}'''+str(data[5])+r'''\end{verbatim}'''+'\n \n'
            main+=r'''\textbf{Mots-clés:}'''+str(data[6])+'\n \n'       
            main+=r'''\textbf{Problématique:}'''+str(data[7])+'\n \n'
            main+=r'''\textbf{Corps du TIPE en français:}'''+str(data[8]).replace('_',"\_")+'\n \n'
            main+=r'''\textbf{Conclusion:}'''+str(data[9])+'\n \n'
            if data[10][-3:]=='pdf':
                main+=r'''\includepdf{'''+str(data[10])+'}\n \n'
            main+=r'''\textbf{Fichier 1:} \begin{verbatim}'''+str(data[10])+'\end{verbatim}\n \n'
            main+=r'''\textbf{Fichier 2:} \begin{verbatim}'''+str(data[12])+'\end{verbatim}\n \n'
        mon_fichier=open('fichier.tex','w')
        footer = r'''\end{document}'''
        main=main.replace('α',r'''$\alpha$''')
        main=main.replace('°',r'''\textdegree ''')
        main=main.replace('ξ',r'''$\xi$''')
        main=main.replace('τ',r'''$\tau$''')
        main=main.replace('δ',r'''$\delta$''')
        main=main.replace('ρ',r'''$\rho$''')
        main=main.replace('Δ',r'''$\Delta$''')
        main=main.replace('=',r'''$=$''')
        main=main.replace('^',r'''\verb?^?''')
        main=main.replace('*',r'''\verb?^?''')
        main=main.replace('γ',r'''$\gamma$''')
        main=main.replace('λ',r'''$\lambda$''')
        main=main.replace('β',r'''$\beta$''')
        main=main.replace('π',r'''$\pi$''')
        main=main.replace('√',r'''$\sqrt{}$''')
        main=main.replace('∑',r'''$\sum$''')
        main=main.replace('Π',r'''$\Pi$''')
        main=main.replace('₁',r'''$_1$''')
        main=main.replace('₂',r'''$_1$''')
        main=main.replace('₃',r'''$_1$''')
        main=main.replace('₄',r'''$_1$''')
        main=main.replace('ω',r'''$\omega$''')
        main=main.replace('∞',r'''$\infty$''')
        main=main.replace('̅',r'''-''')
        main=main.replace('˙',r'''.''')
        main=main.replace('’',"'")
        main=main.replace('$$',"$ $")
        main=main.replace('θ',r'''$\theta$''')

        content = header + main + footer
        mon_fichier.write(content)
        mon_fichier.close()
    else:
        from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.lib.pagesizes import letter


        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleH = styles['Heading1']
        story = []

        pdf_name = 'formulaire_tipe_ptsi_dorian.pdf'
        doc = SimpleDocTemplate(
                pdf_name,
                pagesize=letter,
                bottomMargin=.4 * inch,
                topMargin=.6 * inch,
                rightMargin=.8 * inch,
                leftMargin=.8 * inch)
        for ligne in lignes[3:-1]:
            data=ligne.split(";")
            print(data[0])
            main=str(data[0])+r''' '''+str(data[1])+'<br/><br/>'
            main+=str(data[2])+'<br/><br/>'
            main+=r'''Résumé en anglais:<br/>'''+str(data[3])+ "<br/><br/>"
            main+=r'''Bibliographie commentée:<br/>'''+str(data[4])+ "<br/><br/>"
            main+=r'''Références bibliographiques:<br/>'''+str(data[5])+r''''''+ "<br/><br/>"
            main+=r'''Mots-clés:<br/>'''+str(data[6])+ "<br/><br/>"
            main+=r'''Problématique:<br/>'''+str(data[7])+ "<br/><br/>"
            main+=r'''Corps du TIPE en français:<br/>'''+str(data[8]).replace('_',"\_")+ "<br/><br/>"
            main+=r'''Conclusion:<br/>'''+str(data[9])+'<br/><br/>'
            main+=r'''Fichier 1:<br/>'''+str(data[10])+'<br/> <br/>'
            main+=r'''Fichier 2:<br/>'''+str(data[12])+'<br/> <br/>'
            content=main
            P = Paragraph(content, styleN)
            story.append(P)
            story.append(PageBreak())
        doc.build(
            story,
        )

contenu(0)

    



