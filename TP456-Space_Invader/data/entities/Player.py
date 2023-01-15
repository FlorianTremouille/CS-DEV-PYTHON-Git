"""
Class s'occupant du joueur.
Date : 22/12/2022
Florian Trémouille et Hugo Miaglia
"""


from tkinter import Canvas
from pynput.keyboard import Key, HotKey, Listener
from time import time

from .Bullet import Bullet

class Player:

    bullet_speed = 3
    fire_cooldown = 0.5   #Temps en secondes
    last_fire_time = 0


    def __init__(self, canvas: Canvas, x: int = 400, y: int = 650, width: int = 50, height: int = 50, color: str = 'blue'):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.is_alive = True
        self.__remaining_lives = 3
        self.__god_mod = False

        self.bind_inputs()

    def get_canvas(self):
        return self.__canvas

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_width(self):
        return self.__width
    
    def get_height(self): 
        return self.__height   

    def get_color(self):
        return self.__color
    
    def set_id(self, id : int):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_is_alive(self):
        return self.is_alive

    def get_life_remaining(self):
        return self.__remaining_lives

    def set_god_mod(self, value : bool):
        """Permet de passer ou d'enlever le joueur du mode invincible."""
        self.__god_mod = value
        self.__shining_life_value = value
        self.shining_life()

    def shining_life(self):
        """Fait clignotter la vie restante."""
        if self.__shining_life_value:
            self.__canvas.itemconfig('life_text', fill='blue')
            self.__canvas.after(150, lambda : self.__canvas.itemconfig('life_text', fill='red'))
            self.__canvas.after(300, lambda : self.shining_life())

    def bind_inputs(self):
        """Initialise le Listener du clavier"""
        self.__listener = Listener(on_press=self.on_press_handlers) 
        self.__listener.start() 

    def on_press_handlers(self, key):
        """Permet d'executer les fonctions correspondantes aux touches pressées."""
        if self.is_alive:
            if (key == Key.left):
                self.move_left()
            if (key == Key.right):
                self.move_right()
            if (key == Key.space):
                actual_time = time()
                if actual_time - self.last_fire_time >= self.fire_cooldown:
                    self.last_fire_time = actual_time
                    self.fire_bullet()
            if 'char' in dir(key):
                if (key.char == 'l'):
                    self.add_life()
                if (key.char == 'g'):
                    self.force_god_mod()

    def move_left(self):
        """Déplace le joueur a gauche."""
        if self.__canvas.coords('player')[0]-25 > 25:
            x = -20
            y = 0            
            self.__canvas.move('player', x , y)

    def move_right(self):
        """Déplace le joueur a droite."""
        if self.__canvas.coords('player')[0]+25 < 775:
            x = 20
            y = 0
            self.__canvas.move('player', x, y) 

    def fire_bullet(self):
        """
        Réalise le tir du joueur.
        Crée l'objet de classe Bullet avec les paramètres adaptés au joueur.
        """
        bullet_tag = 'p_bullet' 
        actual_player_coords = self.__canvas.coords(self.__id)
        x = actual_player_coords[0]
        y = actual_player_coords[1]
        Bullet(self.__canvas, bullet_tag, x, y).fire(self.bullet_speed)

    def add_life(self):
        """Permet d'ajouter une vie"""
        self.__remaining_lives += 1
        self.__canvas.itemconfig('life_text', text='Vies restantes : ' + str(self.__remaining_lives))

    def force_god_mod(self):
        """Permet de passer en mode invincible ou de s'en enlever."""
        if not self.__god_mod:
            self.set_god_mod(True)
            self.__canvas.itemconfig('life_text', text='God Mod')
        else:
            self.set_god_mod(False)
            self.__canvas.itemconfig('life_text', text='Vies restantes : ' + str(self.__remaining_lives))

    def check_for_collision(self):
        """Observe si le joueur subit une collision."""
        if self.get_is_alive():
            c = self.get_canvas().coords(self.get_id())
            w = self.__width
            h = self.__height
            entitites = self.get_canvas().find_overlapping(c[0] - w/2, c[1] - h/2, c[0] + w/2, c[1] + h/2)      

            for widget in entitites:
                pass
                for tag in self.get_canvas().gettags(widget):
                    if 'e_bullet' == tag:
                        self.life_loose()
                        self.__canvas.delete(widget)
                    if 'enemy' == tag:
                        self.player_dead()

            self.get_canvas().after(30, lambda: self.check_for_collision())

    def life_loose(self):
        """fait perdre une vie au joueur et le tue si il n'en as plus."""
        if self.__god_mod == False:
            if self.__remaining_lives == 0 :
                self.player_dead()
            else:
                self.__remaining_lives -= 1
                self.set_god_mod(True)
                self.__canvas.itemconfig('life_text', text='Vies restantes : ' + str(self.__remaining_lives))
                self.__canvas.after(5*1000, lambda: self.set_god_mod(False))

    def player_dead(self):
        """Défini l'etat du joueur comme mort."""
        self.is_alive = False