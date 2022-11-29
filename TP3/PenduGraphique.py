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
from FctsGraphique import FindWord, RempStrJeu, AffiMotATrouver, CallInput, LettreIsIn
import tkinter as Tk

def majmot():
    LabelMotATrouver.config(text = AffiMotATrouver(motATrouver))

def gagne():
    LabelMotATrouver.config(text = "GAGNE !!! Le mot était bel et bien " + motATrouver)

def perdu():
    LabelMotATrouver.config(text = "PERDU !!! Le mot était " + mot)



def ClickProposer():
    global NbError
    global MaxError
    global motATrouver
    global mot
    global lstLettresAppel

    LabelInformations.config(text = "")
    Lettre = Entree.get()

    if LettreIsIn(Lettre,mot) == True:
        motATrouver = RempStrJeu(Lettre,mot,motATrouver)
        majmot()
        if motATrouver == mot:
            gagne()

    if Lettre in lstLettresAppel:
        LabelInformations.config(text = "Lettre déjà appelée")
    

    if LettreIsIn(Lettre,mot) == False and Lettre not in lstLettresAppel:
        NbError += 1
        LabelCoupsRestants.config(text = "Il vous reste " + str(MaxError-NbError) + " erreurs possibles.")
        Canvas.create_image(0,0, anchor = Tk.NW, image = Images[NbError-1])


    if Lettre not in lstLettresAppel:
        lstLettresAppel.append(Lettre)

    if NbError == MaxError:
        perdu()
    Entree.delete(0)
    



Fichier = 'mots.txt'
mot, motATrouver = FindWord(Fichier)
lstLettresAppel =[]

motATrouver = RempStrJeu(mot[0],mot, motATrouver)

NbError = 0
MaxError = 8

Window = Tk.Tk()
Window.title('Jeu du pendu')
Window.geometry('800x600')

imagePath = "./TP3/images_PENDU/bonhommeX.gif"
Images = []
for i in range(1,9):
    Images.append(Tk.PhotoImage(file ="./TP3/images_PENDU/bonhomme" + str(i) + ".gif"))

BouttonProposer = Tk.Button(Window, text="Proposer", command=ClickProposer)
BouttonProposer.pack(side= "left")

Canvas = Tk.Canvas(Window)
Canvas.pack(side= "right", padx= 5, pady= 5)

Entree = Tk.Entry(Window)
Entree.pack(side="left")

LabelMotATrouver = Tk.Label(Window, text="Mot a trouver")
LabelMotATrouver.pack()

LabelCoupsRestants = Tk.Label(Window, text="Coups restants")
LabelCoupsRestants.pack()

LabelInformations = Tk.Label(Window, text="")
LabelInformations.pack(side= "bottom")

majmot()

Window.mainloop()