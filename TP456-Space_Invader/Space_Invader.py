"""
Si erreur : "ModuleNotFoundError: No module named 'pynput'"
Relancer l'installeur Python et s'assurer d'avoir coché "Add python to enironment variables"
Faire dans la console :
    python -m ensurepip
    pip install pynput
    
TO DO :
"""

import tkinter as Tk
from time import sleep

from entities.Game import Game


def Restart(canvas):
    canvas.delete('all')
    # canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
    # canvas.pack(anchor=Tk.CENTER, side="top")
    Jeu = Game(canvas)

def LeaveGame():
    Window.destroy()


Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1200x800'  )

score=Tk.Label(Window,text='Score : 0')
score.pack(anchor=Tk.N, side="left", padx= 5, pady= 5) # 

NbVies=Tk.Label(Window,text="Vies : 3")
NbVies.pack(anchor= Tk.N, side="right", padx= 5, pady= 5) # 

QuitBtn=Tk.Button(Window,text="Quitter",command=LeaveGame)
QuitBtn.pack(anchor=Tk.S, side="right", padx= 5, pady= 5)

RestartBtn=Tk.Button(Window, text="Recommencer une partie", command=(lambda: Restart(canvas)))  #NE FONCTIONNE PAS
RestartBtn.pack(anchor=Tk.S, side="left", padx= 5, pady= 5)

# GameImage=Tk.PhotoImage(file='fond.gif')
canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
# canvas.create_image(0,0,anchor='nw',image=GameImage)
canvas.pack(anchor=Tk.CENTER, side="top", padx= 5, pady= 5)

Jeu = Game(canvas)
Window.mainloop()