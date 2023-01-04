"""
Class s'occupant des ennemies basiques.
"""
from tkinter import Canvas

class BasicEnemy:

    def __init__(self, canvas: Canvas, width: int = 50, height: int = 50, color: str = 'red'):
        self.__canvas = canvas
        self.__width = width
        self.__height = height
        self.__color = color
        self.__is_alive = True

    def get_canvas(self):
        return self.__canvas

    def get_id(self):
        return self.__id

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_color(self):
        return self.__color

    def get_check_for_collision_after_id(self):
        return self.__check_for_collision_after_id
    
    def set_check_for_collision_after_id(self, id):
        self.__check_for_collision_after_id = id

    def get_is_alive(self):
        return self.__is_alive

    def set_id(self, id):
        self.__id = id        

    def check_for_collision(self):        
        continue_check = False
        c = self.get_canvas().coords(self.get_id())        
        entitites = self.get_canvas().find_overlapping(c[0], c[1], c[2], c[3]) # a changer a cause du polygone       
        
        for widget in entitites:
            for tag in self.get_canvas().gettags(widget):
                if 'p_bullet' == tag:
                    self.die_and_destroy_bullet(widget)
                else: 
                    continue_check = True
        if (continue_check and self.get_is_alive()):    
            self.set_check_for_collision_after_id(self.get_canvas().after(30, lambda: self.check_for_collision()))

    def die_and_destroy_bullet(self, bullet):
        self.__is_alive = False
        self.__canvas.after_cancel(self.get_check_for_collision_after_id())
        self.__canvas.delete(self.get_id())
        self.__canvas.delete(bullet)