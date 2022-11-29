'''
Fonctions du programme du pendu TP3
29/11/2022
Author : Hugo MIAGLIA & Florian TREMOUILLE
'''
from random import randint

def FindWord(Fichier):
    '''Ouvre un fichier .txt et renvoie un mot.
    Fichier doit etre sous la forme : fichier.txt
    Retourne le mot et une string de underscore avec autant de caractère que le mot.'''
    fichier = open('./TP3/' + Fichier,'r')
    mots = fichier.readlines()
    fichier.close()
    i = randint(0,len(mots)-1)
    mot = mots[i][:-1]

    underscoreSTR = ""
    for l in range(0,len(mot)):
        underscoreSTR += "_"
    return mot, underscoreSTR

def RempStrJeu(Letter,mot,strAcompleter):
    '''
    Regarde si la lettre est dans le mot.
    Retourne la str du jeu en cours.
    Letter est une str de 1 de long.
    mot est une str.
    strAcompleter est une str.
    '''
    if Letter in mot:
        for i,l in enumerate(mot):
            if l == Letter:
                strAcompleter = strAcompleter[:i] + mot[i] + strAcompleter[i+1:]
    return strAcompleter 

def LettreIsIn(Letter,mot):
    LettreIsIn = False
    if Letter in mot:
        LettreIsIn = True
    return LettreIsIn

def AffiMotATrouver(motcache):
    toPrint = ""
    for i in motcache:
        toPrint += i + " "
    return toPrint


def CallInput():
    lettre = "-1"
    while isinstance(lettre,str) == False or len(lettre) != 1:
        lettre = input("Tapez une lettre : ")
    return lettre

def DejaAppel(lettre, lettresappelee):
    if lettre in lettresappelee:
        return True
    return False