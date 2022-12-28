"""
Class s'occupant du joueur.
"""
from tkinter import Canvas
from pynput.keyboard import Key, Listener
from time import time

from .Bullet import Bullet

class Player:

    bullet_speed = 3
    bullet_fired = 0
    fire_cooldown = 0.5   #Temps en secondes
    last_fire_time = 0


    def __init__(self, canvas: Canvas, x: int = 350, y: int = 650, width: int = 50, height: int = 50, color: str = 'blue'):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color

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

    def bind_inputs(self):        
        listener = Listener(on_press=self.on_press_handlers) 
        listener.start()         
            
    def on_press_handlers(self, key):
        if (key == Key.left):
            self.move_left()
        if (key == Key.right):
            self.move_right()
        if (key == Key.space):
            Actual_Time = time()
            if Actual_Time - self.last_fire_time >= self.fire_cooldown:
                self.last_fire_time = Actual_Time
                self.fire_bullet()

    def move_left(self):
        if self.__canvas.coords('player')[0] > 25:
            x = -20
            y = 0            
            self.__canvas.move('player', x , y)

    def move_right(self):
        if self.__canvas.coords('player')[2] < 775:
            x = 20
            y = 0
            self.__canvas.move('player', x, y) 

    def fire_bullet(self):
        bullet_tag = 'p_bullet_{0}'.format(self.bullet_fired)
        self.bullet_fired += 1
        actual_player_coords = self.__canvas.coords('player')
        x = actual_player_coords[0] + (self.__width / 2)
        y = actual_player_coords[1]
        Bullet(self.__canvas, bullet_tag, x, y).fire(self.bullet_speed)
