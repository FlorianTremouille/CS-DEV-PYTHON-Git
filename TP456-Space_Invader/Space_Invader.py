import tkinter as Tk
from entities.World import World

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
canvas.pack(side= "left", padx= 5, pady= 5)

# Vaisseau = Canvas.create_rectangle(0, 648, 50, 698, fill='blue')

map = World(canvas)
PLAYER = map.W_Player.getCP()

dENNEMI = map.W_Ennemis
# Ennemi = canvas.create_rectangle(0, 0, 50, 50, fill='red')

def EnnemiMove(way):
    x = 50
    CoordsLast = canvas.coords(dENNEMI.values()[-1])
    CoordsFirst = canvas.coords(dENNEMI.values()[0])
    
    if CoordsLast[2] > 750 and way == 1 :
        way = -1
    elif CoordsFirst[0] < 50 and way == -1 :
        way = 1

    if way == 1:
        canvas.move(dENNEMI,x,0)
        Window.after(500,lambda: EnnemiMove(way))
    elif way == -1:
        canvas.move(dENNEMI,-x,0)
        Window.after(500,lambda: EnnemiMove(way))


def left(e):
   x = -20
   y = 0
   canvas.move(PLAYER, x, y)
   map.W_Player.set(canvas.coords(PLAYER)[2],canvas.coords(PLAYER)[1])

def right(e):
   x = 20
   y = 0
   canvas.move(PLAYER, x, y)
   map.W_Player.set(canvas.coords(PLAYER)[2],canvas.coords(PLAYER)[1])


def ProjMove(proj):  # fonction qui fait bouger les projectiles
    # proj est un canvas.rectangle
    y = -1
    canvas.move(proj,0,y)
    if canvas.coords(proj)[1] == 0 :
        canvas.delete(proj)
        return
    Window.after(5,lambda : ProjMove(proj))

def Tir(e) :
    x = map.W_Player.getx() - (map.W_Player.getw())/2
    y = map.W_Player.gety()
    PlayerProj = map.W_Player.PlayerProj_Init(canvas,x,y)
    ProjMove(PlayerProj)


# Bind the move function
Window.bind("<Left>", left)
Window.bind("<Right>", right)
Window.bind("<space>", Tir)

# Initialisation
Window.after(100,lambda: EnnemiMove(1))
Window.after(100,ProjMove)

Window.mainloop()