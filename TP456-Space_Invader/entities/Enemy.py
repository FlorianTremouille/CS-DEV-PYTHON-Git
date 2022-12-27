"""
Class s'occupant des ennemies.
"""
from tkinter import Canvas

class Enemy:

    def __init__(self, canvas: Canvas, width: int = 50, height: int = 50, color: str = 'red'):
        self.__canvas = canvas
        self.__width = width
        self.__height = height
        self.__color = color

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

    def get_interval_id(self):
        return self.__interval_id

    def set_id(self, id):
        self.__id = id

    def check_for_collision(self):
        c = self.__canvas.coords(self.__id)
        if (len(c) > 0):
            entitites = self.__canvas.find_overlapping(c[0], c[1], c[2], c[3])
            if (len(entitites) > 1):
                print(entitites)
                for widget in entitites:
                    for tag in self.__canvas.gettags(widget):
                        print(tag)
                        if 'p_bullet_' == tag[0:9]:
                            self.die_and_kill_bullet(entitites[1])
                        elif 'player' == tag:
                            print('PERDU')
                            #Crée methode de defaite

        self.__interval_id = self.__canvas.after(30, lambda: self.check_for_collision())

    def die_and_kill_bullet(self,bullet):
        self.__canvas.after_cancel(self.__interval_id) #A quoi ca sert ?
        self.__canvas.delete(self.__id)
        self.__canvas.delete(bullet)