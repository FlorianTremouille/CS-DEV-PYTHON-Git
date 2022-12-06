import tkinter as Tk

Window = Tk.Tk()
Window.title('Space INVADATEUR')
Window.geometry('1000x800')

Canvas = Tk.Canvas(Window, width='800', height='700', bg = 'black')
Canvas.pack(side= "left", padx= 5, pady= 5)

Vaisseau = Canvas.create_rectangle(0, 648, 50, 698, fill='blue')
Ennemi = Canvas.create_rectangle(0, 0, 50, 50, fill='red')

def EnnemiMove(way):
    x = 20
    Coords = Canvas.coords(Ennemi)
    
    if Coords[2] > 750 and way == 1 :
        way = -1
    elif Coords[0] < 50 and way == -1:
        way = 1

    if way == 1:
        Canvas.move(Ennemi,x,0)
        Window.after(1000,EnnemiMove(way))
    elif way == -1:
        Canvas.move(Ennemi,-x,0)
        Window.after(1000,EnnemiMove(way))


def left(e):
   x = -20
   y = 0
   Canvas.move(Vaisseau, x, y)

def right(e):
   x = 20
   y = 0
   Canvas.move(Vaisseau, x, y)

# Bind the move function
Window.bind("<Left>", left)
Window.bind("<Right>", right)

# Initialisation
EnnemiMove(1)

Window.mainloop()