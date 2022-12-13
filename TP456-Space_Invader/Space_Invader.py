import tkinter as Tk
from entities.World import World

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
canvas.pack(side= "left", padx= 5, pady= 5)

map = World(canvas)

PLAYER_CANVAS = map.W_Player.Can_Player
ENNEMI_TAG_LST = map.W_Ennemis.get()
ENNEMIS_OBJECT = map.W_Ennemis

def EnnemiMove(way):
    x = 5
    y = 0
    CoordsLast = canvas.coords(ENNEMI_TAG_LST[-1])
    CoordsFirst = canvas.coords(ENNEMI_TAG_LST[0])

    if CoordsLast[2] > 750 and way == 1 :
        way = -1
    elif CoordsFirst[0] < 50 and way == -1 :
        y = 50
        way = 1
    
    for ennemi in ENNEMI_TAG_LST:
        if way == 1:
            canvas.move(ennemi,x,y)
        elif way == -1:
            canvas.move(ennemi,-x,y)
    Window.after(42,lambda: EnnemiMove(way))


def left(e):
   x = -20
   y = 0
   canvas.move(PLAYER_CANVAS, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(PLAYER_CANVAS, x, y)

def ProjMove(proj):
    y = -20
    canvas.move(proj,0,y)
    Window.after(200,lambda : ProjMove(proj))

def Tir(e) :
    PlayerProj = map.W_Player.PlayerProj_Init(canvas)
    ProjMove(PlayerProj)


# Bind the move function
Window.bind("<Left>", left)
Window.bind("<Right>", right)
Window.bind("<space>", Tir)

# Initialisation
# Window.after(1000,ENNEMIS_OBJECT.EnnemiMove(canvas,1))
EnnemiMove(1)
Window.after(100,lambda: EnnemiMove(1))
Window.after(100,ProjMove)

Window.mainloop()