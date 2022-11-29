'''
Programme du pendu TP3
29/11/2022
Author : Hugo MIAGLIA & Florian TREMOUILLE
crayon
essaim
souris
abeille
clavier
sobriete
indignite
telephone
'''

from Fcts import FindWord, RempStrJeu, AffiMotATrouver, CallInput, LettreIsIn

Fichier = 'mots.txt'
mot, motATrouver = FindWord(Fichier)
lstLettresAppel =[]

motATrouver = RempStrJeu(mot[0],mot, motATrouver)
AffiMotATrouver(motATrouver)

NbError = 0
MaxError = 8

while motATrouver != mot:
    if NbError == MaxError:
        print("PERDU !!!")
        print("Le mot était " + mot)
        break

    else:
        Lettre = CallInput()
        motATrouver = RempStrJeu(Lettre,mot,motATrouver)
        LettreJuste = LettreIsIn(Lettre,mot)
        AffiMotATrouver(motATrouver)

        if motATrouver == mot:
            print("GAGNE !!!")
            print("Le mot était bien" , motATrouver)
            break

        if Lettre in lstLettresAppel:
            print('Lettre déjà appelée')

        if LettreJuste == False and Lettre not in lstLettresAppel:
            NbError += 1
            print(Lettre, " n'est pas dans le mot.")
            print("Il vous reste ", MaxError-NbError," erreurs possibles.")

        lstLettresAppel.append(Lettre)
