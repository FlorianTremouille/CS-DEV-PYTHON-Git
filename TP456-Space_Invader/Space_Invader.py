"""
Fichier qui s'occupe de lancement du jeu
Date : 30/12/2022
Florian Trémouille et Hugo Miaglia

Si erreur : "ModuleNotFoundError: No module named 'pynput'"
Installer le module pynput.
Relancer l'installeur Python et s'assurer d'avoir coché "Add python to enironment variables"
Faire dans la console :
    python -m ensurepip
    pip install pynput
"""
import os
import tkinter as Tk

from data.entities.Game import Game
from data.entities.Score import Score

working_dir = os.path.dirname(__file__)
os.chdir(working_dir)

frame_menu : Tk.Frame
frame_game : Tk.Frame
best_score : Tk.Label
about : Tk.Tk
bg_game_img : Tk.PhotoImage
game : Game
canvas : Tk.Canvas
menu_font : tuple = ('Helvetica', '12')

def start_menu():
    """Crée et affiche la fenêtre de lancement."""
    global frame_menu, bg_frames_img, menu_font, best_score

    frame_menu = Tk.Frame(window, bg= "red")

    bg_menu = Tk.Label(frame_menu, image= bg_frames_img)
    bg_menu.place(x = 0, y = 0)

    about_btn = Tk.Button(frame_menu,text="A propos", command=display_about)
    about_btn.pack()

    game_title = Tk.Label(frame_menu, text="SPACE INVADER", font=menu_font)
    game_title.pack(padx= 100, pady= (100,100))

    best_score_text = "Meilleur score : \n" + str(Score().get_best())
    best_score = Tk.Label(frame_menu, text = best_score_text, bg=None, font=menu_font)
    best_score.pack(padx= 100, pady= (0,0))

    del_best = Tk.Button(frame_menu, text="Supprimer le dernier meilleur score.", font = ('Helvetica', '8') , command=delete_last_best_score)
    del_best.pack(padx= 100, pady= (0,0))

    play_btn = Tk.Button(frame_menu, text="Jouer",command=start_game)
    play_btn.pack(anchor=Tk.S, side="left", padx= 5, pady= (50,5))

    quit_btn=Tk.Button(frame_menu,text="Quitter",command=leave_game)
    quit_btn.pack(anchor=Tk.S, side="right", padx= 5, pady= (50,5))

    frame_menu.pack(fill=Tk.BOTH)

def display_about():
    """Crée et affiche la fenêtre 'A Propos'."""
    global about

    try:
        about
        about.destroy()
    except:
        pass

    about = Tk.Tk()
    about.title('A propos')

    project_title = Tk.Label(about, text="PROJET CS DEV PYTHON")
    author_title = Tk.Label(about, text="Hugo MIAGLIA et Florian TRÉMOUILLE")

    project_title.pack(padx= 100)
    author_title.pack(padx= 100)

    about.mainloop()

def delete_last_best_score():
    global best_score
    if len(Score().read_bests()) > 1: 
        Score().delete_last_best()
        best_score_text = "Meilleur score : \n" + str(Score().get_best())
        best_score.config(text= best_score_text)

def start_game(): 
    """Crée la fenêtre de jeu et l'initialise."""
    global game, frame_game, bg_game_img, bg_frames_img, canvas
    frame_menu.destroy()
    
    frame_game = Tk.Frame(window)

    canvas = Tk.Canvas(frame_game, width='800', height='700', highlightthickness = 0)
    canvas.create_image(400,350,image=bg_game_img)
    canvas.pack(anchor=Tk.CENTER, side="top")

    frame_game_actions = Tk.Frame(frame_game)

    bg_menu = Tk.Label(frame_game_actions,image= bg_frames_img)
    bg_menu.place(x = 0, y = 0)

    RestartBtn=Tk.Button(frame_game_actions, text="Recommencer une partie", command=restart)
    RestartBtn.pack(anchor=Tk.S, side="left", padx= 5, pady= 5)

    quit_btn=Tk.Button(frame_game_actions,text="Quitter",command=leave_game)
    quit_btn.pack(anchor=Tk.S, side="right", padx= 5, pady= 5)

    frame_game_actions.pack(fill=Tk.BOTH, side=Tk.BOTTOM)

    frame_game.pack(padx=0,pady=0)

    game = Game(canvas)
    window.update()

def restart():
    """Relance une partie."""
    global game, canvas
    Score(canvas).reset_score()
    del game
    frame_game.destroy()
    start_game()

def leave_game():
    """Ferme la fenetre."""
    window.destroy()


window = Tk.Tk()
window.title('Space INVADATEUR')

bg_game_img= Tk.PhotoImage(file='data/images/game_bg.gif')
bg_frames_img= Tk.PhotoImage(file='data/images/frame_bg.gif')


start_menu()
window.mainloop()