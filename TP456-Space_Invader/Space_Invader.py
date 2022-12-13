import tkinter as Tk
from entities.World import World

VITESSE_ENNEMI_X = 5
VITESSE_ENNEMI_Y = 50

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

score=Tk.Label(Window,text='Score: 0')
score.pack(anchor="nw", side="left", padx= 5, pady= 5)

NbVies=Tk.Label(Window,text="Vies: 3")
NbVies.pack(anchor= "ne", side="right", padx= 5, pady= 5)

canvas = Tk.Canvas(Window, width='800', height='700', bg = 'gray')
canvas.pack(side= "bottom", padx= 5, pady= 5)



# Vaisseau = Canvas.create_rectangle(0, 648, 50, 698, fill='blue')

map = World(canvas)
PLAYER_CANVAS = map.W_Player.getCP()
ENNEMI_TAG_LST = map.W_Ennemis.get()
ENNEMIS_OBJECT = map.W_Ennemis

# Ennemi = canvas.create_rectangle(0, 0, 50, 50, fill='red')



def left(e):
    if canvas.coords(PLAYER_CANVAS)[0] > 25:
        x = -20
        y = 0
        canvas.move(PLAYER_CANVAS, x, y)
        map.W_Player.set(canvas.coords(PLAYER_CANVAS)[2],canvas.coords(PLAYER_CANVAS)[1])

def right(e):
    if canvas.coords(PLAYER_CANVAS)[2] < 775:
        x = 20
        y = 0
        canvas.move(PLAYER_CANVAS, x, y)
        map.W_Player.set(canvas.coords(PLAYER_CANVAS)[2],canvas.coords(PLAYER_CANVAS)[1])


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