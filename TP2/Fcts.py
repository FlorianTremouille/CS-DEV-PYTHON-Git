# coding:Latin-1
'''
Fonctions du programme d'automate TP2 
22/11/2022
Author : Hugo MIAGLIA & Florian TREMOUILLE
Python : 2.7.17 (Nous nous sommes rendu compte en fin de scéance qu'il était utilisé par défaut. Désolé.)
'''

#Importation du dictionnaire a partir d'un auter fichier.
import dico
dictionnaire = dico.dicowords

#Définition des fonctions
def AffichageTable(Table):
    """
    Affichage d'une liste de liste sous la forme dun tableau. Chaque sous-liste est print à la suite.
    Table est une liste de liste.
    """
    for Lst in Table:
        print(Lst)
    return

def Init(inputS,stateS):
    """
    Définit et retourne la table de transition et initialise le premier état.
    inputS et stateS sont des tuples.
    """
    Table_Transition = []
    Table_Sortie =[]
    for state in stateS:
        Table_Transition.append([])
        for input in inputS:
            Table_Transition[state].append(8)

    Table_Transition[0][0]=1
    Table_Transition[0][4]=4
    Table_Transition[1][1]=1
    Table_Transition[1][2]=2
    Table_Transition[2][1]=2
    Table_Transition[2][3]=3
    Table_Transition[3][0]=5
    Table_Transition[3][4]=7
    Table_Transition[3][5]=9
    Table_Transition[4][3]=3
    Table_Transition[5][1]=5
    Table_Transition[5][2]=6
    Table_Transition[6][1]=6
    Table_Transition[6][5]=9
    Table_Transition[7][5]=9
    Table_Transition[8]=-1
    Table_Transition[9]=1

    return Table_Transition, 0


def MotsEnChiffres(Phrase):
    """
    Renvoie une liste ordonée du type de chaque mots de la phrase, codé selon le dictionnaire
    Phrase est du type string.
    """
    #Ecriture de la phrase en lowercase pour correspondre au dictionnaire.
    Phrase = Phrase.lower()

    #PAS DANS LA CONSIGNE - Correctif pour ajouter un point si il a été oublié.
#    if Phrase[-1] != ".":
#        Phrase = Phrase + " ."

    #Ajoute un espace entre le point et le dernier mot si il n'est pas présent.
    #Sert au découpage de
    if Phrase[-1] == "." and Phrase[-2] != " ":
        Phrase = Phrase[0:-1]
        Phrase = Phrase + " ."

    LstPhrase = Phrase.split(" ")
    LstCode = []
    for word in LstPhrase:
        if word in dictionnaire :
            LstCode.append(dictionnaire[word])
        else:
            print("Certains mots de la phrase sont inconnus.")
            return []
    return LstCode

#Automate
def Automate(Table_Transition,Act_State,Phrase):
    """
    Table_Transition est la table de transition(type : liste de listes). Act_State est l'état de départ (type : int). Phrase (type : string).
    Renvoie si la phrase est correcte ou non.
    """
    phrase_code = MotsEnChiffres(Phrase)
    for i in phrase_code:
        Act_State = Table_Transition[Act_State][i]
        if isinstance(Table_Transition[Act_State],int):
            if Table_Transition[Act_State] == -1:
                print("Phrase NON correcte.")
                break
            else:
                print("Phrase correcte.")
                break