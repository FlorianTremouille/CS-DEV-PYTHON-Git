"""
Class s'occupant des ennemies basiques.
"""
from tkinter import Canvas

from .EnemyType import EnemyType
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

    def set_id(self, id):
        self.__id = id        

    def check_for_collision(self):        
        if self.__is_alive:
            c = self.get_canvas().coords(self.get_id())
            entitites = self.get_canvas().find_overlapping(c[4], c[7], c[20], c[1]) # adapté au polygone     
            
            for widget in entitites:
                for tag in self.get_canvas().gettags(widget):
                    if 'p_bullet' == tag:
                        self.touch_and_destroy_bullet(widget)
            self.get_canvas().after(30, lambda: self.check_for_collision())

    def touch_and_destroy_bullet(self, bullet):
        self.__is_alive = False
        self.__canvas.delete(self.get_id())
        self.__canvas.delete(bullet)
        self.update_score(self.__class__.__name__)

    def update_score(self, enemy_type: str):        
        score = Score(self.__canvas)
        score.update_score(enemy_type)        
