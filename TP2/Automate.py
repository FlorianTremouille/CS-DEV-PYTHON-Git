# coding:Latin-1
'''
Programme d'automate TP2 
22/11/2022
Author : Hugo MIAGLIA & Florian TREMOUILLE
Python : 2.7.17 (Nous nous sommes rendu compte en fin de scéance qu'il était utilisé par défaut. Désolé.)
'''

from Fcts import Init, AffichageTable, MotsEnChiffres, Automate

#Saisie utilisateur protegee. On demande un element non nul.
phrase = raw_input("Tapez votre phrase : ") 
while phrase == "":
    print("Tapez une phrase !!!")
    phrase = raw_input("Tapez votre phrase : ") 

#Reference de la valeur numerique correspondant a chaque type de mot dans l'ordre :
#   Article - Adjectif - Nom - Verbe - Nom Propre - Point
inputS = (0,1,2,3,4,5)

#Reference des etats.
stateS = (0,1,2,3,4,5,6,7,8,9)

#Creation de la table de transition et initialisation de l'etat actuelle a 0.
Table_Transition,Act_State = Init(inputS, stateS)
#AffichageTable(Table_Transition)

Automate(Table_Transition,Act_State,phrase)