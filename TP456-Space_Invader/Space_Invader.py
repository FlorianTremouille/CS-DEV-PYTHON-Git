import tkinter as Tk
from entities.World import World

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
canvas.pack(side= "left", padx= 5, pady= 5)

# Vaisseau = Canvas.create_rectangle(0, 648, 50, 698, fill='blue')

map = World(canvas)
PLAYER = map.p.player
canvas.pack()
Ennemi = canvas.create_rectangle(0, 0, 50, 50, fill='red')

def EnnemiMove(way):
    x = 50
    Coords = canvas.coords(Ennemi)
    
    if Coords[2] > 750 and way == 1 :
        way = -1
    elif Coords[0] < 50 and way == -1 :
        way = 1

    if way == 1:
        canvas.move(Ennemi,x,0)
        Window.after(500,lambda: EnnemiMove(way))
    elif way == -1:
        canvas.move(Ennemi,-x,0)
        Window.after(500,lambda: EnnemiMove(way))


def left(event):
   x = -20
   y = 0
   canvas.move(PLAYER, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(PLAYER, x, y)

# Bind the move function
Window.bind("<Left>", left)
Window.bind("<Right>", right)

# Initialisation
Window.after(100,lambda: EnnemiMove(1))

Window.mainloop()