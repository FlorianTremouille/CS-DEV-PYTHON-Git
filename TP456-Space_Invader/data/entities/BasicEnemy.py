"""
Class s'occupant des ennemies basiques.
Date : 30/12/2022
Florian Trémouille et Hugo Miaglia
"""
from tkinter import Canvas

from .Score import Score

class BasicEnemy:

    def __init__(self, canvas: Canvas, scale: int = 50, color: str = 'darkred'):
        self.__canvas = canvas
        self.__scale = scale
        self.__color = color
        self.__is_alive = True

    def get_canvas(self):
        return self.__canvas

    def get_id(self):
        return self.__id

    def get_scale(self):
        return self.__scale

    def get_color(self):
        return self.__color

    def get_is_alive(self):
        return self.__is_alive

    def set_id(self, id : int) -> bool:
        self.__id = id      

    def check_for_collision(self):
        """Observe si l'ennemi subit une collision."""
        c = self.get_canvas().coords(self.get_id())
        if self.__is_alive and len(c) !=0 :
            c = self.get_canvas().coords(self.get_id())
            entitites = self.get_canvas().find_overlapping(c[4], c[7], c[20], c[1]) # Coordonnées adaptées au polygone.     
            
            for widget in entitites:
                for tag in self.get_canvas().gettags(widget):
                    if 'p_bullet' == tag:
                        self.touch_and_destroy_bullet(widget)
            self.get_canvas().after(30, lambda: self.check_for_collision())

    def touch_and_destroy_bullet(self, bullet : int):
        """
        Permet d'executer l'action souhaité lorsque l'alien est touché par un objet Bullet et détruit l'objet l'ayant touché.
        Pour un ennemi classique, il meurt.
        Pour l'ennemi BOSS, il perd une vie.
        """
        self.__is_alive = False
        self.__canvas.delete(self.get_id())
        self.__canvas.delete(bullet)
        self.update_score(self.__class__.__name__)

    def update_score(self, enemy_type: str):
        """Actualise les scores à la suite de l'élimination d'un ennemi."""    
        score = Score(self.__canvas)
        score.update_score(enemy_type)