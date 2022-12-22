"""
TO DO :
OVERLAPPING
MULTIPLE ENNEMI RAW
LINE 51-56 : INDEX ERROR
"""

import tkinter as Tk

from entities.Game import Game

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

score=Tk.Label(Window,text='Score: 0')
score.pack(anchor="nw", side="left", padx= 5, pady= 5)

NbVies=Tk.Label(Window,text="Vies: 3")
NbVies.pack(anchor= "ne", side="right", padx= 5, pady= 5)

# GameImage=Tk.PhotoImage(file='fond.gif')
canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
# canvas.create_image(0,0,anchor='nw',image=GameImage)
canvas.pack(side= "bottom", padx= 5, pady= 5)

Game(canvas)

Window.mainloop()